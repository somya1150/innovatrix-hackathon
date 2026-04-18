from django.urls import path
from . import views

app_name = 'myweb'

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login_page, name='login'),
    path('register/', views.register_user, name='register'),
]