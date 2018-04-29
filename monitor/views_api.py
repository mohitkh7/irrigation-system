import json
from django.http import JsonResponse
from django.core import serializers

# from rest_framework import viewsets
# from .serializers import DeviceControlSerializer, DeviceStateSerializer, DeviceStateListSerializer

from .models import DeviceState, DeviceControl


def check_device_moisture(request):
    last = last_status(request)
    last_state_of_device = json.loads(last.content.decode('utf-8'))
    current_moisture = last_state_of_device['moisture']
    state, lower_threshold_moisture, upper_threshold_moisture, mode = get_device_detail()
    # It is following inverse value logic
    # To check whether mode is automated if not then skip
    print(mode)
    if mode == 'automated':
        if current_moisture < lower_threshold_moisture:
            turn_device(1)
            print("Device ON")

        if current_moisture > upper_threshold_moisture:
            turn_device(0)
            print("Device OFF")


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
    res['moisture'] = q.moisture
    res['status'] = q.status
    return JsonResponse(res)


def all_status(request):
    query = DeviceState.objects.all()
    s = serializers.serialize("json", query)
    return JsonResponse({'res': s})


def create_status(request):
    moisture = request.GET['moisture']
    status = request.GET['status']
    device = DeviceState(moisture=moisture, status=status)
    device.save()
    check_device_moisture(request)
    res = {'status': 1, 'message': 'device status updated'}
    return JsonResponse(res)


def read_instruction(request):
    device_control = DeviceControl.objects.get(id=1)
    set_state = device_control.set_state
    return JsonResponse({'set_state': set_state})


def get_device_detail():
    try:
        device = DeviceControl.objects.first()
        lower_threshold = device.lower_threshold
        upper_threshold = device.upper_threshold
        state = device.set_state
        mode = device.mode
    except:
        print("There is an Exception")
        lower_threshold = 15
        upper_threshold = 50
        state = False
        mode = 'automated'

    return (state, lower_threshold, upper_threshold, mode)


def update_mode(request):
    device = DeviceControl.objects.first()
    set_mode_to = request.GET['mode']
    device.mode = set_mode_to
    device.save()
    return JsonResponse({'msg':'Mode Updated'});


def update_set(request):
    device = DeviceControl.objects.first()
    set = request.GET['set']
    device.set_state = set
    device.save()
    return JsonResponse({'msg':'Set_State Updated '+set});