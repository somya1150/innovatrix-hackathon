from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myweb'

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/', views.login_page, name='login'),
    path('register/', views.login_page, name='register'),
    path('shop/', views.shop, name='shop'),
    path('sell/', views.sell, name='sell'),
    path('impact/', views.impact, name='impact'),
    path('cart/', views.cart, name='cart'),
    path('user/', views.user, name='user'),
    path('logout/',views.logoutuser,name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
