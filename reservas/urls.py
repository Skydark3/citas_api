from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CitaViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'citas', CitaViewSet)

urlpatterns = router.urls
