from django.views.generic import TemplateView
from rest_framework import status, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response


from .fusiontables import API_KEY, LocationFTService, LOCATION_FIELD_NAME, TABLE_ID
from .models import Location
from .serializers import LocationSerializer


class HomeView(TemplateView):
    template_name = "locations/index.html"

    def get_context_data(self, **kwargs):
        # Include the already stored addresses when reloading
        context = super().get_context_data()
        context['locations'] = Location.objects.all()
        context['api_key'] = API_KEY
        context['ft_location_field_name'] = LOCATION_FIELD_NAME
        context['ft_table_name'] = TABLE_ID
        return context


class LocationViewSet(viewsets.ModelViewSet):
    """API endpoint that view or edit locations"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request):
        response = super().create(request)
        if response.status_code == status.HTTP_201_CREATED:
            # Create row in Google Fusion Tables, launch an exception on fail
            LocationFTService().create_location(request.data['lat'], request.data['lon'])
        return response

    @list_route(methods=['post'])
    def empty(self, request):
        """Empty the location objects from database"""
        Location.objects.all().delete()
        LocationFTService().empty_locations()
        return Response({'status': 'empty locations'})
