from django.views.generic import TemplateView


from .models import Location


class HomeView(TemplateView):
    template_name = "locations/index.html"

    def get_context_data(self, **kwargs):
        # Include the already stored addresses when reloading
        context = super().get_context_data()
        context['locations'] = Location.objects.all()
        return context
