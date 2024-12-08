from django.db import transaction
from django import forms
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from django.core.paginator import Paginator
from django.http import JsonResponse
import datetime
from taxi.helpers.taxi_helpers import parse_range, parse_range_float

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import NotFound, ValidationError, APIException, ParseError
# from rest_framework import status
# from django.conf import settings
from taxi.serializers.taxi_serializers import TaxiResponseSerializer

import uuid
import re
import base64
from ast import literal_eval
import math

from taxi.models import TaxiResponse


class TaxiViewSet(ViewSet):
    
    @api_view(['GET'])
    @transaction.atomic
    def getAll(request):
        payment_type = request.query_params.get('paymenttype')
        [min_distance, max_distance, min_amounts, max_amounts, min_ptime, max_ptime, min_dtime, max_dtime] = [None, None, None, None, None, None, None, None]
        try:
            min_distance, max_distance = parse_range_float(request.query_params.get('distance'))
            min_amounts, max_amounts = parse_range_float(request.query_params.get('amounts'))
            min_ptime, max_ptime = parse_range(request.query_params.get('ptime'))
            min_dtime, max_dtime = parse_range(request.query_params.get('dtime'))
        except ValueError:
            return Response({"error": "Invalid range format for distance, amounts, and time. Use 'min-max' format for distance and amounts."}, status=400)
        if(min_ptime):
            min_ptime = datetime.datetime.fromtimestamp(min_ptime / 1000)
        if(max_ptime):
            min_ptime = datetime.datetime.fromtimestamp(max_ptime / 1000)
        if(min_dtime):
            min_ptime = datetime.datetime.fromtimestamp(min_dtime / 1000)
        if(max_dtime):
            min_ptime = datetime.datetime.fromtimestamp(max_dtime / 1000)
        page_number = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('limit', 10))
        
        record = TaxiResponse.objects.all()
        if(payment_type):
            record = record.filter(payment_type=payment_type)
        if min_distance != None:
            record = record.filter(trip_distance__gte=min_distance)  # Filter distance >= min_distance
        if max_distance != None:
            record = record.filter(trip_distance__lte=max_distance)  # Filter distance <= max_distance
        if min_amounts != None:
            record = record.filter(fare_amount__gte=min_amounts)  # Filter distance >= min_distance
        if max_amounts != None:
            record = record.filter(fare_amount__lte=max_amounts)  # Filter distance <= max_distance
        if min_ptime != None:
            record = record.filter(pickup_datetime__gte=min_ptime)  # Filter distance >= min_distance
        if max_ptime != None:
            record = record.filter(pickup_datetime__lte=max_ptime)  # Filter distance <= max_distance
        if min_dtime != None:
            record = record.filter(dropoff_datetime__gte=min_dtime)  # Filter distance >= min_distance
        if max_dtime != None:
            record = record.filter(dropoff_datetime__lte=max_dtime)  # Filter distance <= max_distance
        
        record_count =  record.count()
        record = record[((page_number-1)*page_size):page_size*page_number]
        
        serializer = TaxiResponseSerializer(record, many=True)
        return Response({
        "message": "Successfully get data",
        'count': record_count,
        'num_pages': int((record_count/page_size) +1 if record_count//page_size !=0 else record_count/page_size),
        'current_page': page_number,
        'results': serializer.data,  # Serialisasi ke list
        })