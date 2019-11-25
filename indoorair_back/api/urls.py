from django.urls import path

from . import views

urlpatterns = [



# ---- homepage -----

    path('api/version', views.api_version, name='api_version'),
# ---- gateway-----

    path('api/regsiter', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', views.LoginAPI.as_view(), name='login_api'),
    path('api/logout', views.post_logout_api, name='logout_api'),
# ---- dashboard -----

    path('api/dashboard', views.DashboardAPI.as_view(), name='dashboard_apis'),
# ---- instrument -----


    path('api/instruments', views.get_instruments_list_api, name='instruments_api'),
    # path('api/instruments/create', views.post_instruments_create_api, name='instrument_create_api'),
    path('api/instrument/<int:id>', views.InstrumentRetrieveAPI.as_view(), name='i_retrieve_api'),
    path('api/instrument/<int:id>/update', views.InstrumentUpdateAPI.as_view(), name='i_update_api'),

# ---- report -----

     path('report/api/1', views.download_csv_report_01_temperature_sensor_api, name="download_csv_report_01_temperature_sensor_api"),
# ---- sensor -----

     path('api/sensor/<int:id>', views.SensorRetrieveAPI.as_view(), name='sensor_retrieve_api'),
# ---- user profile -----

    path('profile', views.profile_retrieve_page, name='profile_retrieve_page'),
    path('profile/update', views.profile_update_page, name='profile_update_page'),

]


# path   网站的前缀
]


# path   网站的前缀
