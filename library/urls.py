from django.urls import path
from .views import BookListCreateApiView, BookRetrieveUpdateDeleteApiView

urlpatterns = [
    # generic views url patterns

    # path('books/', BookListCreateApiView.as_view()),
    # path('books/<int:pk>/', BookRetrieveUpdateDeleteApiView.as_view()),
    # path('books/', BooksListAPiView.as_view()),
    # # path('books/', book_list_api_view),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('books/<int:pk>/', BookRetrieveApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),

    # ApiViews url pattenrs
    path('books/', BookListCreateApiView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteApiView.as_view())
]
