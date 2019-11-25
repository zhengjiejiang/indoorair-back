from django.urls import path

from . import views

urlpatterns = [

    path('api/version', views.api_version, name='api_version'),

]


# path   网站的前缀
