from django.urls import path
from .views import import_data, export_data


urlpatterns = [
    path('import-data/', import_data, name='import_data'),
    path('export-data/', export_data, name='export_data'),
]

