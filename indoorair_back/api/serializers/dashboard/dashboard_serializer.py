from rest_framework import serializers
from django.contrib.auth.models import User # STEP 1: Import the user
import statistics
from foundation.models import TimeSeriesDatum, Sensor, Instrument

class DashboardSerializer(serializers.BaseSerializer):
    def get_values(self,sensor_name, insturments):
        sensor = Sensor.objects.get(
            name = sensor_name,
            instrument = instrument,
        )

        temp_values = TimeSeriesDatum.objects.filter(sensor = temp_sensor).values_list('value', flat=Ture)
        return values

    def get_statistics(self, values):
        try:
            statistics.mode(temp_values)
        except Exception as e:
            mode = "NF"

        try:
             statistics.median(temp_values)
        except Exception as e:
             mode = "NF"

        try:
             statistics.mean(temp_values)
        except Exception as e:
             mean = "NF"

    def to_representation(self, instruments):

        results = []
        for instrument in instruments:


            temp_values = self.get_values('Temperature', instrument)
            hum_values = self.get_values('Humidity', instrument)
            pressure_values = self.get_values('Pressure', instrument)
            co2_values = self.get_values('Co2', instrument)
            tvoc_values = self.get_values('TVOC', instrument)

            try:
                statistics.mode(temp_values)
            except Exception as e:
                mode = "NF"


            hum_sensor = Sensor.objects.get(
                name = "Humidity",
                instrument = instrument,
            )

            hum_values = TimeSeriesDatum.objects.filter(sensor = hum_sensor).values_list('value', flat=Ture)

            try:
                statistics.mode(hum_values)
            except Exception as e:
                mode = "NF"



        return {

        }
