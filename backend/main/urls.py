from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .views import login, CameraDetail, ViolationDetail, VehicleDetail

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cameras', CameraViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'violations', ViolationViewSet)
router.register(r'hubs', HubViewSet)
router.register(r'documents', VehicleDocumentViewSet)
router.register(r'route-logs', VehicleRouteLogViewSet)
router.register(r'scan-logs', ScanLogViewSet)
router.register(r'hub-logs', HubLogViewSet)

urlpatterns = [
    path('login/', login, name='login'),
    path('cameras/<str:camID>/', CameraDetail, name='ViolationCount'),
    path('violations/<str:camID>/', ViolationDetail, name='ViolationDetail'),
    path('vehicles/<str:chipID>/', VehicleDetail, name='VehicleDetail'),

]

urlpatterns += router.urls
