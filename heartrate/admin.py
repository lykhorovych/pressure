from django.contrib import admin
from django.contrib.admin import ModelAdmin
from heartrate.models import HeartRate

# Register your models here.
class HeartRateAdmin(ModelAdmin):
    class Meta:
        model = HeartRate
        list_display = ('sistolic', 'diastolic', 'pulse')


admin.site.register(HeartRate, HeartRateAdmin)
