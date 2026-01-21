# branches/urls.py
from django.urls import path
from . import views


app_name = 'branches'

urlpatterns = [
    path('', views.branch_list, name='branch_list'),
    path('<int:pk>/delete/', views.branch_delete, name='branch_delete'),
]
