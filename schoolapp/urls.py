from django.urls import path
from . import views

app_name = 'schoolapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login_view'),
    path('user_info/', views.user_info, name='user_info'),
    path('/logout', views.logout_view, name='logout')
]
