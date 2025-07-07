from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from services.r2_storage import R2Storage
from rest_framework import status
from botocore.exceptions import ClientError  # Add this import

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def all_books(request):
    books = Book.objects.all().order_by("-created_at")
    books_serializer = BookSerializer(books, many=True)
    return Response({
        'books' : books_serializer.data
    })
    
    
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_book(request):
    print("actual data: ",request.data)
    data = request.data
    print("data is : ",data)
    book_serializer = BookSerializer(data=data)
    if not book_serializer.is_valid():
        return Response(book_serializer.errors, status=400)
    book = book_serializer.save()

    return Response({
        'message': 'Book added successfully',
        'book': BookSerializer(book).data
    }, status=201)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        
        # Delete the PDF from R2 storage if pdf_key exists
        if book.pdf_key:
            r2 = R2Storage()
            try:
                r2.delete(book.pdf_key)
            except ClientError as e:
                print(f"Error deleting PDF from storage: {e}")
        
        book.delete()
        return Response({'message': 'Book deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def get_upload_url(request):
    """
    Expects JSON: { "file_name": "filename.pdf", "content_type": "application/pdf", "folder": "books" }
    Returns: { "upload_url": ..., "key": ... }
    """
    file_name = request.data.get("file_name")
    content_type = request.data.get("content_type", "application/octet-stream")
    folder = request.data.get("folder", "")
    if not file_name:
        return Response({"error": "file_name required"}, status=400)
    key = f"{folder}/{file_name}" if folder else file_name
    r2 = R2Storage()
    upload_url = r2.generate_upload_url(key, content_type=content_type)
    return Response({"upload_url": upload_url, "key": key})
