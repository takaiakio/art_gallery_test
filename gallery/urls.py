# gallery/urls.py

from django.urls import path
from .views import art_list, upload_art, delete_art

urlpatterns = [
    path('', art_list, name='art_list'),
    path('upload/', upload_art, name='upload_art'),
    path('delete/<int:pk>/', delete_art, name='delete_art'),  # pkを使用して削除するためのパスを追加
]
