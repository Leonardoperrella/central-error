from rest_framework import routers
from stone.api.views import ErrorViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('errors', ErrorViewSet)
