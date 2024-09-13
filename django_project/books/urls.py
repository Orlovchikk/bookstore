from django.urls import include, path, re_path

from .views import BookDetailView, BookListView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<str:slug>/", BookDetailView.as_view(), name="book_detail"),
]
