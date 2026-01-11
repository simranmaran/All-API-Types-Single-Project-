# from rest_framework.routers import DefaultRouter
# from .views import MovieViewSet

# router = DefaultRouter()
# router.register('viewset/movies', MovieViewSet)

# urlpatterns = router.urls


from rest_framework import routers
from .views import MovieViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

urlpatterns = router.urls
