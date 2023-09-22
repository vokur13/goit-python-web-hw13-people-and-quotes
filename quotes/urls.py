from django.urls import path

from .views import (
    QuotesListView,
    AuthorDetailView,
    TagDetailView,
    QuoteCreateView,
    TagCreateView,
    AuthorCreateView,
)

app_name = "quotes"

urlpatterns = [
    path("tag/new/", TagCreateView.as_view(), name="tag_new"),
    path("author/new/", AuthorCreateView.as_view(), name="author_new"),
    path("quote/new/", QuoteCreateView.as_view(), name="quote_new"),
    path("author/<slug:slug>", AuthorDetailView.as_view(), name="author_detail"),
    path("tag/<slug:slug>", TagDetailView.as_view(), name="tag_detail"),
    path("", QuotesListView.as_view(), name="home"),
]
