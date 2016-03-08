from django.views.generic import TemplateView
from rest_framework import viewsets


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
