from django.urls import path

from .views import BookDetailView, BookListView, SearchResultsListView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path("<str:slug>/", BookDetailView.as_view(), name="book_detail"),
]
