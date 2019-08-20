from rest_framework import routers
from . import views


router = routers.DefaultRouter()


router.register('photos', views.ObjViewSet, 'photos')
# router.register('ships', views.ShipViewSet, 'ships')


urlpatterns = router.urls
