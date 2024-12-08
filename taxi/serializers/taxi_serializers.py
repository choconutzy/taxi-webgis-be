from rest_framework.serializers import ModelSerializer
from taxi.models import TaxiResponse

class TaxiResponseSerializer(ModelSerializer):
    class Meta:
        model = TaxiResponse
        fields = '__all__'  # or specify fields like ['id', 'vendor_id']