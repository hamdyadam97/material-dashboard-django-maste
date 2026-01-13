from django.urls import path
from .views import login_view, dashboard_view,create_employee

app_name = 'accounts'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create-employee/', create_employee, name='create_employee'),
]
