from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

# router = routers.DefaultRouter()
# router.register('MyAPI', views.ApprovalsView)
urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('multi/', views.multiple_choices, name='multi_choice')
    # path('form/', views.custcontact, name='custform'),
    # path('api/', include(router.urls)),
    # path('status/', views.approvereject),
]

# below code is for InputFiles app
if settings.DEBUG:
    urlpatterns += static(settings.UPLOADED_URL, document_root=settings.UPLOAD_ROOT)