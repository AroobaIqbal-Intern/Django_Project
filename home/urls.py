from django.contrib import admin
from django.urls import path ,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact',views.contact,name='contact') ,
    path('services/ice-cream/', views.ice_cream_view, name='ice_cream'),
    path('services/softy/', views.softy_view, name='softy'),
    path('services/family-pack/', views.family_pack_view, name='family_pack'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

]