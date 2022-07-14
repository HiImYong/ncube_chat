# chat/urls.py
from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    # path('gen_qr/', views.qrcode, name='qrcode'),
    # path('<str:room_name>/kick_user', views.kick_user, name='kick_user'),

]