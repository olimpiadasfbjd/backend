from rest_framework import routers

from .views import (DataViewSet)

router = routers.DefaultRouter()
router.register(r'data', DataViewSet)