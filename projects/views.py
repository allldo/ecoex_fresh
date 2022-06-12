from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from projects.models import City


@login_required
def air_quality(request):
    city_objects = City.objects.all()
    context = {'city_objects': city_objects}
    return render(request, 'landing/air_qual.html', context)
