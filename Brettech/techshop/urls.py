from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('bread', views.bread, name='bread'),
    path('checkout', views.checkout, name='checkout'),
    path('drinks', views.drinks, name='drinks'),
    path('events', views.events, name='events'),
    path('faqs', views.faqs, name='faqs'),
    path('frozen', views.frozen, name='frozen'),
    path('household', views.household, name='household'),
    path('kitchen', views.kitchen, name='kitchen'),
    path('login', views.login, name='login'),
    path('mail', views.mail, name='mail'),
    path('payment', views.payment, name='payment'),
    path('pet', views.pet, name='pet'),
    path('privacy', views.privacy, name='privacy'),
    path('products', views.products, name='products'),
    path('services', views.services, name='services'),
    path('short-codes', views.shortcodes, name='short-codes'),
    path('single', views.single, name='single'),
    path('vegetables', views.vegetables, name='vegetables')
]
