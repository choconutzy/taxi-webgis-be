from django.db import models
from mysite.models import BaseModel
#from django.contrib.gis.db import models

# Create your models here.
																	

class TaxiResponse(BaseModel):

  id = models.IntegerField(null=False, primary_key=True)
  vendor_id = models.CharField(max_length=256, null=False)
  pickup_datetime = models.DateTimeField(null=False)
  dropoff_datetime = models.DateTimeField(null=False)

  passenger_count = models.IntegerField()
  trip_distance = models.FloatField(max_length=256, default=0.0)
  pickup_longitude = models.FloatField(max_length=256, default=0.0)
  pickup_latitude = models.FloatField(max_length=256, default=0.0)
  store_and_fwd_flag = models.CharField(max_length=5)
  dropoff_longitude = models.FloatField(max_length=256, default=0.0)
  dropoff_latitude = models.FloatField(max_length=256, default=0.0)
  payment_type = models.CharField(max_length=5)
  fare_amount = models.FloatField(max_length=256, default=0.0)
  mta_tax = models.FloatField(max_length=256, default=0.0)
  tip_amount = models.FloatField(max_length=256, default=0.0)
  tolls_amount = models.FloatField(max_length=256, default=0.0)
  total_amount = models.FloatField(max_length=256, default=0.0)
  imp_surcharge = models.FloatField(max_length=256, default=0.0)
  extra = models.CharField(max_length=256, default=0.0)
  rate_code = models.IntegerField()

  def __str__(self):
    return self.vendor_id


  class Meta:
    db_table = 'taxi'
    