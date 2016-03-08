from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response


from .models import Location
from .serializers import LocationSerializer


class HomeView(TemplateView):
    template_name = "locations/index.html"

    def get_context_data(self, **kwargs):
        # Include the already stored addresses when reloading
        context = super().get_context_data()
        context['locations'] = Location.objects.all()
        return context


class LocationViewSet(viewsets.ModelViewSet):
    """API endpoint that view or edit locations"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @list_route(methods=['post'])
    def empty(self, request):
        """Empty the location objects from database"""
        Location.objects.all().delete()
        return Response({'status': 'empty locations'})
