from .import views
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'),
    path('landing/', views.landing, name='landing'),
    path('list/', views.book_list, name='book_list'),
    path('new/', views.book_create, name='book_create'),
    path('edit/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]
