from django.db import models

class Location(models.Model):
    # We use here a simple approach of storing the Lat/Lon using
    # Floats instead of GIS DB extensions for the sake of avoiding
    # installing more dependencies
    lat = models.FloatField(null=False)
    lon = models.FloatField(null=False)
    address = models.CharField(max_length=255)

    def __str__(self):
        return "({lat}, {lon}){address}".format(
            address=" " + self.address if len(self.address) > 0 else "",
            lat=self.lat,
            lon=self.lon)
