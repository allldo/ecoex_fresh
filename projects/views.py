from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from projects.models import Project


@login_required
def air_quality(request):
    return render(request, 'landing/air_qual.html')
