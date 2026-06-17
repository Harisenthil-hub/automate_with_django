from django.urls import path
from .views import send_email, track_click, track_open, track_dashboard, track_stats

urlpatterns = [
    path('send-email/',  send_email, name='send_email'),
    path('track/click/<unique_id>/', track_click, name='track_click'),
    path('track/open/<unique_id>/', track_open, name='track_open'),
    path('track/dashboard/', track_dashboard, name='track_dashboard'),
    path('track/stats/<int:pk>/', track_stats, name='track_stats'),
]
