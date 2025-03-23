from django.urls import path
from .views import (
    UserSignupView, SellerSignupView, login_view,
    PropertyDetailView, book_property, PropertyListCreateView
)

house_urlpatterns = [
    # Authentication URLs
    path('signup/user/', UserSignupView.as_view(), name='user-signup'),
    path('signup/seller/', SellerSignupView.as_view(), name='seller-signup'),
    path('login/', login_view, name='login'),

    # Property Management URLs
    
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),
    path('properties/<int:property_id>/book/', book_property, name='book-property'),

    # Booking a Property
    path('properties/<int:property_id>/book/', book_property, name='book-property'),
]

urlpatterns = house_urlpatterns
