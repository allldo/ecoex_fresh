from django.shortcuts import render

from landing.models import FAQ, Service

# Create your views here.


def main_page(request):
    context = {}
    context['Service'] = Service.objects.all()
    context['FAQ'] = FAQ.objects.all()
    return render(request, 'landing/main_page.html', context)