from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalsView)
urlpatterns = [
    path('form/', views.custcontact, name='custform'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
