from rest_framework import serializers


class InstrumentUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    location = serializers.CharField()

    def update(self,object,validated_data):
        name = validated_data.get('name')
        location = validated_data.get('location')
        object.name = name
        object.location = location 
        object.save()
