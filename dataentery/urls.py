
from .views import import_data
from django.urls import path

urlpatterns = [
    path('import-data/',import_data,name='import_data'),
]
