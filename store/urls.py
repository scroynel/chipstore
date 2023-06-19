from django.urls import path

from .views import CreateRatingView, ReviewView, ProductListView, ProductDetailView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('ratings/', CreateRatingView.as_view()),
    path('reviews/', ReviewView.as_view()),
]