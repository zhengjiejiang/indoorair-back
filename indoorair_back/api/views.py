

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import status, response, views

from gateway.serializers import RegisterSerializer, LoginSerializer
from dashboard.serializers import DashboardSerializer
from foundations.models import Instrument,TimeSeriesDatum,Sensor
from instrument.serializers import InstrumentRetrieveSerializer
from sensor.serializers import SensorRetrieveSerializer
import csv







# ---- homepage -----



def api_version(request):
    return JsonResponse({'version': 'Melody'})


#----gateway----
"""
gateway/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login, logout
from rest_framework import views, status, response

from gateway.serializers import RegisterSerializer, LoginSerializer




class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data,
        )



class LoginAPI(views.APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={
            'request': request,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                 'details': 'You have been logged in successfully!'
            },
        )






#---dashboard---

class DashboardAPI(views.APIView):
    def get(self, request):
        instruments = Instrument.objects.filter(user=request.user)
        serializer = DashboardSerializer(instruments)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )



# ---instrument ---
def get_instruments_list_api(request):
    instruments = Instrument.objects.filter(user=request.user)
    output = []
    for instrument in instruments.all():
        output.append({
            'id': instrument.id,
            'name': instrument.name,
        })
    return JsonResponse({
        'instruments': output
    })

class InstrumentRetrieveAPI(views.APIView):
    def get(self, request, id):
        instrument = Instrument.objects.get(id=int(id))
        serializer = InstrumentRetrieveSerializer(instrument, many=False)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

class InstrumentUpdateAPI(views.APIView):
    def put(self, request, id):
        instrument = Instrument.objects.get(id=id)
        serializer = InstrumentUpdateSerializer(instrument, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'Updated instrument'
            }
        )




#---report---

def download_csv_report_01_temperature_sensor_api(request):
    # https://docs.djangoproject.com/en/2.2/howto/outputting-csv/

    data = TimeSeriesDatum.objects.filter(
        sensor__name="Temperature",
        sensor__instrument__user=request.user,
    )

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="temperature_data.csv"'

    # Connect our response object with our CSV writer object.
    writer = csv.writer(response)

    # This is the header row
    writer.writerow(['sensor_name', 'sensor_id', 'time', 'value',])

    # Let us go through all our data and generate our CSV file.
    for datum in data:
        writer.writerow([datum.sensor.name, datum.sensor.id, datum.time, datum.value])

    return response












#---sensor---

class SensorRetrieveAPI(views.APIView):
    def get(self, request, id):
        sensor = get_object_or_404(Sensor, id=int(id))
        serializer = SensorRetrieveSerializer(sensor)
        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )





#---user profile---


def profile_retrieve_page(request):
    return render(request, "pages/userprofile/retrieve.html", {})



def profile_update_page(request):
    return render(request, "pages/userprofile/update.html", {})
