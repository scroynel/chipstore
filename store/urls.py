from django.urls import path

from .views import ProductView, CreateRatingView

urlpatterns = [
    path('products/', ProductView.as_view({'get': 'list'})),
    path('products/<str:slug>/', ProductView.as_view({'get': 'retrieve'})),
    path('ratings', CreateRatingView.as_view())
]