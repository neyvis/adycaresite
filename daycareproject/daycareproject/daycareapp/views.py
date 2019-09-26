from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render

from .models import Educator, Class


def index(request):
    return render(request, 'base.html')



def find_educator(request, educator_id):
    return render("You're looking at educator %s." % educator_id)


def educator_list(request):
    educators_qs = Educator.objects.all()
    context = {
        'educator_list': educators_qs,
    }
    return render(request, 'educators.html', context)


class EducatorList(ListView):
    model = Educator
    context_object_name = 'my_favorite_educators'
    template_name = 'index.html'


    def get_queryset(self):
        """Return the educator list."""
        return Educator.objects.all()


class ClassDetail(DetailView):

    model = Class

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['educator_list'] = Educator.objects.all()
        return context

class EducatorDetail(DetailView):

    context_object_name = 'educator'
    queryset = Educator.objects.all()

class AboutView(TemplateView):
    template_name = "about.html"