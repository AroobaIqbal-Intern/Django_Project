from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    
    # Services dropdown URLs
    path('services/ice-cream/', views.ice_cream_view, name='ice_cream'),
    path('services/softy/', views.softy_view, name='softy'),
    path('services/family-pack/', views.family_pack_view, name='family_pack'),

    # Cart URL (optional)
    path('signup/', views.signup_view, name='signup'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-placed/', views.order_placed_view, name='order_placed'),
]
