from django.urls import path
from .import views



urlpatterns = [
    path('',views.simple_form, name='simple_form'),
    path('payment_form/', views.payment_form, name='payment_form'),
]