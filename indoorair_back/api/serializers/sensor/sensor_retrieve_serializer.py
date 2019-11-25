from rest_framework import serializers


class SensorRetrieveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
