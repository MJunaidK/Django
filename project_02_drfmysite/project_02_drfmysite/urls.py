"""
URL configuration for project_02_drfmysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('actions', ActionViewSet, basename='actions')
router.register('comedies', ActionViewSet, basename='comedies')

urlpatterns = [
    path('', include(router.urls)), 
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
