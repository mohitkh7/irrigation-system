from django.contrib import admin
from .models import DeviceState, DeviceControl


# Register your models here.
class DeviceStateAdmin(admin.ModelAdmin):
    readonly_fields = ('time',)


class DeviceControlAdmin(admin.ModelAdmin):
    list_display = ('set_state', 'lower_threshold', 'upper_threshold', 'mode')

    def has_add_permission(self, request):
        base_add_permission = super(DeviceControlAdmin, self).has_add_permission(request)
        if base_add_permission:
            # if there's already an entry, do not allow adding
            if DeviceControl.objects.exists():
                    return False
            return True


admin.site.register(DeviceState, DeviceStateAdmin)
admin.site.register(DeviceControl, DeviceControlAdmin)

