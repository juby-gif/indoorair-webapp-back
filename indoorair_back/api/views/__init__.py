from api.views.homepage.views import VersionAPI
from api.views.gateway.views import RegisterAPI, LoginAPI ,post_logout_api
from api.views.dashboard.views import DashboardAPI
from api.views.instrument.views import get_instruments_list_api,InstrumentRetrieveAPI,InstrumentUpdateAPI
from api.views.profile_api.views import get_profile_retrieve_api,post_profile_update_api
from api.views.report.views import download_csv_report_01_temperature_sensor_api
from api.views.sensor.views import SensorRetrieveAPI
