"""irrigation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path, include
from rest_framework import routers

from .views import index, log, LogView, DeviceStateCreateView, DeviceControlUpdateView

'''
REST Api
from .views import DeviceControlViewSet, DeviceStateViewSet,
router = routers.DefaultRouter()
router.register(r'control', DeviceControlViewSet)
router.register(r'state', DeviceStateViewSet)
'''

urlpatterns = [
    path('', index, name='index'),
    path('log/', log, name='log'),
    path('history/', LogView.as_view(), name="history"),
    path('test/', DeviceStateCreateView.as_view(), name="test"),
    path('settings/<int:pk>/', DeviceControlUpdateView.as_view(), name="settings")
]
