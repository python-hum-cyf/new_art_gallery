from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Painter

# Create your views here.
class HelloView(TemplateView):
    template_name = 'hello.html'

class PaintersListView(TemplateView):
    template_name = 'painters_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['painters'] = Painter.objects.all()

        return context
