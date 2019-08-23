from rest_framework import routers

from backend.views import (DataViewSet)

router = routers.DefaultRouter()
router.register(r'data', DataViewSet)