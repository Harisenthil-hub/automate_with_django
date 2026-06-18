from django.urls import path
from .views import compress


urlpatterns = [
    path('compress/', compress, name='compress'),
]
