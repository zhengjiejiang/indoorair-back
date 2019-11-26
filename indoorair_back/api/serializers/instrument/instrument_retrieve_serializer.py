from rest_framework import serializers
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout
from foundation.models import Instrument, Sensor, TimeSeriesDatum


class  InstrumentRetrieveSerializer(serializers.Serializer):


    id = serializers.IntegerField(read_only=True)
    location = serializers.CharField()
    serial_number = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)

    def create(self, validated_data):

        location = validated_data.get('location', None)
        instrument = Instrument.objects.create(location=location)
        return instrument


    def update(self, object, validated_data):

        object.url = validated_data.get('url')
        object.save()
        return object
