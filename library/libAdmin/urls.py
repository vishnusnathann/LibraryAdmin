from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
path('', views.loginAction, name='login'),
path('addbook', views.add_Book, name='add_Book'),
path('welcome', views.welcome, name='add_Book'),
path('listBooks', views.listBooks, name='listBooks'),
path('edit_book/<int:requested_id>', views.edit_book, name='edit_book'),
path('delete_book/<int:requested_id>', views.delete_book, name='delete_book'),
]