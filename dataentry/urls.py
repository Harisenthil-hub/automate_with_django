from django.urls import path
from .views import import_data


urlpatterns = [
    path('import-data/', import_data, name='import_data'),
]

