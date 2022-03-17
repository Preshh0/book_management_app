from django.urls import path
from .views import BookList, BookDetail

app_name = 'book_management'

urlpatterns = [
    path('book/', BookList.as_view(), name="book_view"),
    path('booklist/', BookDetail.as_view(), name='book_detail')
]