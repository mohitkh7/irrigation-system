from .models import DeviceState, DeviceControl
from rest_framework import serializers


class DeviceStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceState
        # fields = ('humidity', 'status', 'time')
        fields = '__all__'


class DeviceStateListSerializer(serializers.ListSerializer):
    child = DeviceStateSerializer()
    allow_null = True
    many = True


class DeviceControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceControl
        fields = ('set_state',)
