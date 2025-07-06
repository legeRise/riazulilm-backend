from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_books, name='all_books'),
    path('add-book/', views.add_book, name='add_book'),
    path('delete-book/<str:book_id>/', views.delete_book, name='delete_book'),
    path('get-upload-url/', views.get_upload_url, name='get_upload_url'),
]