from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf import settings
from taxi.models import TaxiResponse

# Register your models here.
@admin.register(TaxiResponse)
class TaxiAdmin(admin.ModelAdmin):
    search_fields = (
    'vendor_id',
    )
    readonly_fields = (
    'id', 'vendor_id', 'pickup_datetime', 'dropoff_datetime', 'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'store_and_fwd_flag', 'dropoff_longitude', 'dropoff_latitude'
    )
    list_display = (
    'id',
    'vendor_id', 'pickup_datetime', 'dropoff_datetime', 'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'store_and_fwd_flag', 'dropoff_longitude', 'dropoff_latitude'
    )
    def get_fields(self, request, obj=None):
      if request.user.is_superuser:
        return super().get_fields(request, obj)
      else:
        return (
        'id', 'vendor_id', 'pickup_datetime', 'dropoff_datetime', 'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'store_and_fwd_flag', 'dropoff_longitude', 'dropoff_latitude'
        )
