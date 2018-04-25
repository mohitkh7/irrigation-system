from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, generics
from .serializers import DeviceControlSerializer, DeviceStateSerializer

from .models import DeviceState, DeviceControl


def index(request):
    device_state = DeviceState.objects.last()
    print(device_state)
    # return HttpResponse("Om Gang Ganpataye Namah" + str(device_state))
    return HttpResponse(str(device_state))


def log(request):
    devices = DeviceState.objects.all().order_by('-id')
    return render(request, "log.html", {'devices': devices})
    # return HttpResponse("History")


"""
Django REST Api
"""
class DeviceControlViewSet(viewsets.ModelViewSet):
    queryset = DeviceControl.objects.all()
    serializer_class = DeviceControlSerializer


class DeviceStateViewSet(viewsets.ModelViewSet):
    queryset = DeviceState.objects.all()
    serializer_class = DeviceStateSerializer