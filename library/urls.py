from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_list, name='library_list'),
    path('create/', views.library_upload, name='library_upload'),
    path('update/<int:pk>/', views.library_update, name='library_update'),
    path('delete/<int:pk>/', views.library_delete, name='library_delete'),
]
