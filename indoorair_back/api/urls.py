from django.urls import path

from . import views


urlpatterns = [
    #homepage api
    path('api/version', views.VersionAPI.as_view(), name='version_api'),

    #Gateway api
    path('api/register', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', views.LoginAPI.as_view(), name='login_api'),
    path('api/logout', views.post_logout_api, name='logout_api'),

    #Dashboard api
    path('api/dashboard', views.DashboardAPI.as_view(), name='dashboard_api'),
    # #
    #Instrument api
    path('api/instruments', views.get_instruments_list_api, name='instruments_api'),
    path('api/instrument/<int:id>', views.InstrumentRetrieveAPI.as_view(), name='i_retrieve_api'),
    path('api/instrument/<int:id>/update', views.InstrumentUpdateAPI.as_view(), name='i_update_api'),
    #
    # #Report
    path('report/api/1', views.download_csv_report_01_temperature_sensor_api, name="download_csv_report_01_temperature_sensor_api"),
    #
    # #Sensor api
    path('api/sensor/<int:id>', views.SensorRetrieveAPI.as_view(), name='sensor_retrieve_api'),
    #
    # #Profile api
    #
    path('api/profile', views.get_profile_retrieve_api, name='profile_retrieve_api'),
    path('api/profile/update', views.post_profile_update_api, name='profile_update_api'),
]
