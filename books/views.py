from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.conf import settings
from services.supabase_storage import upload_file_to_bucket, get_public_url
import tempfile
from rest_framework import status
import uuid

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
    data = request.data.copy()

    # Step 1: Handle PDF upload
    file = request.FILES.get('pdf_copy')
    if file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            for chunk in file.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name
        pdf_ext = file.name.split('.')[-1]
        pdf_filename = f"book_{uuid.uuid4()}.{pdf_ext}"
        upload_file_to_bucket(
            tmp_path,
            settings.SUPABASE_BUCKET_NAME,
            settings.SUPABASE_FOLDER_NAME,
            pdf_filename
        )
        download_url = get_public_url(
            settings.SUPABASE_BUCKET_NAME,
            settings.SUPABASE_FOLDER_NAME,
            pdf_filename
        )
        data['download_url'] = download_url

    # Step 2: Handle cover image upload
    cover_file = request.FILES.get('cover_image')
    if cover_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            for chunk in cover_file.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name
        cover_ext = cover_file.name.split('.')[-1]
        cover_filename = f"cover_image_{uuid.uuid4()}.{cover_ext}"
        upload_file_to_bucket(
            tmp_path,
            settings.SUPABASE_BUCKET_NAME,
            'cover_images',
            cover_filename
        )
        cover_url = get_public_url(
            settings.SUPABASE_BUCKET_NAME,
            'cover_images',
            cover_filename
        )
        data['cover_image'] = cover_url

    # Step 3: Now validate and save the serializer with URLs included
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
        book.delete()
        return Response({'message': 'Book deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)
