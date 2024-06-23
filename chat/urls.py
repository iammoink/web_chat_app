from django.urls import path
from .views import ChatBoxView

urlpatterns = [
    path('chat/<str:chat_box_name>/', ChatBoxView.as_view(), name='chat')
]