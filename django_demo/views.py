"""
Views for the django demo.
"""
from django.http import HttpResponse


def index(request):
    return HttpResponse(b'')
