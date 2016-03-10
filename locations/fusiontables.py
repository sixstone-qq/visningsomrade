# Fusion tables interface for locations app
from django.conf import settings
import httplib2


from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


# TODO: Put this in settings
API_KEY = settings.LOCATIONS['FUSIONTABLES_API_KEY']
LOCATION_FIELD_NAME = settings.LOCATIONS['LOCATION_FIELD_NAME']
TABLE_ID = settings.LOCATIONS['FUSIONTABLES_TABLE_ID']


class LocationFTService(object):

    def __init__(self):
        # Get the Fusion tables interface with a tuple
        # (service, http_obj)
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            settings.LOCATIONS['FUSIONTABLES_KEYFILE_NAME'],
            scopes='https://www.googleapis.com/auth/fusiontables')

        # Create an httplib2.Http object to handle our HTTP requests and authorize
        # it with the Credentials.
        http = httplib2.Http()
        self.http_client = credentials.authorize(http)

        self.service = build("fusiontables", "v2", http=self.http_client)

    def create_location(self, lat, lon):
        sql_query = """INSERT INTO {table} (Location) VALUES ('{lat} {lon}')""".format(
                           table=TABLE_ID, lat=lat, lon=lon)
        res = self.service.query().sql(
            sql=sql_query).execute(http=self.http_client)
        return res

    def empty_locations(self):
        return self.service.query().sql(
            sql="DELETE FROM {table}".format(
            table=TABLE_ID)).execute(http=self.http_client)
