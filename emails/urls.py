from rest_framework.routers import DefaultRouter
from .views import EmailViewSet


router = DefaultRouter()

router.register(r'emails', EmailViewSet)

urlpatterns = router.urls
