import json
from django.http import JsonResponse
from django.core import serializers

# from rest_framework import viewsets
# from .serializers import DeviceControlSerializer, DeviceStateSerializer, DeviceStateListSerializer

from .models import DeviceState, DeviceControl


def check_device_humidity(request):
    last = last_status(request)
    last_state_of_device = json.loads(last.content.decode('utf-8'))
    current_humidity = last_state_of_device['humidity']
    thresold_lower_humidity = 15
    thresold_upper_humidity = 50
    if current_humidity < thresold_lower_humidity:
        turn_device(1)
        print("Device ON")

    if current_humidity > thresold_upper_humidity:
        turn_device(0)
        print("Device Off")


"""
value == 1:ON ; 0:OFF
"""
def turn_device(value):
    obj = DeviceControl.objects.get(id=1)
    obj.set_state = value
    obj.save()


def last_status(request):
    res = {}
    q = DeviceState.objects.last()
    res['humidity'] = q.humidity
    res['status'] = q.status
    return JsonResponse(res)


def all_status(request):
    query = DeviceState.objects.all()
    s = serializers.serialize("json", query)
    return JsonResponse({'res': s})


def create_status(request):
    humidity = request.GET['humidity']
    status = request.GET['status']
    device = DeviceState(humidity=humidity, status=status)
    device.save()
    check_device_humidity(request)
    res = {'status': 1, 'message': 'device status updated'}
    return JsonResponse(res)


def read_instruction(request):
    device_control = DeviceControl.objects.get(id=1)
    set_state = device_control.set_state
    return JsonResponse({'set_state': set_state})
