from django.urls import include, path
from .views import *

urlpatterns = [
    path('Data/',DataViewSet.as_view(),name='animal')
]
