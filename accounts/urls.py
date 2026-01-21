from django.urls import path
from .views import login_view, dashboard_view, user_list,user_save

app_name = 'accounts'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', user_list, name='user_list'),
    path('user_save', user_save, name='user_save'),
]
