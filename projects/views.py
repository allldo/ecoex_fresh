from django.shortcuts import render

from projects.models import Project


def project_detail(request, id):
    qs = Project.objects.filter(id=id)
    return qs