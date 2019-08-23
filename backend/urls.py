from django.urls import include, path
from backend.views import *

urlpatterns = [
    path('Data/',DataViewSet,name='animal')
]
