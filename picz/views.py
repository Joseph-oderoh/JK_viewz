from django.shortcuts import render
from django.http import HttpResponse
from .models import Images, Locations
# Create your views here.de


def homepage(request):
    return render(request, 'welcome.html')

def gallery(request):
    pictures = Images.get_all()
    locations = Locations.get_all()
    return render(request, 'gallery.html', {'pictures': pictures, 'locations':locations})


def location(request,locale):
    images = Images.filter_by_location(locale)
    return render(request, 'location.html', {'results':images})


