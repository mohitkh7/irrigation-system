from django.db import models


class DeviceState(models.Model):
    humidity = models.IntegerField()
    status = models.BooleanField()
    time = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return "Device => H:"+ str(self.humidity) +" S:" + str(self.status)


class DeviceControl(models.Model):
    set_state = models.BooleanField()

    def __str__(self):
        if self.set_state:
            return "Device ON"
        else:
            return "Device OFF"
