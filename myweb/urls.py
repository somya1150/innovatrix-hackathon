from django.urls import path
from . import views

app_name = 'myweb'

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login_page, name='login'),
    path('shop/', views.shop, name='shop'),
    path('sell/', views.sell, name='sell'),
    path('impact/', views.impact, name='impact'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.login_page, name='register'),

]