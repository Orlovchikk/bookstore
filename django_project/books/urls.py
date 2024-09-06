from django.urls import path, include, re_path

from .views import BookListView, BookDetailView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<str:slug>/", BookDetailView.as_view(), name="book_detail"),
]
