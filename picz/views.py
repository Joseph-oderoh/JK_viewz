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


def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        res = Images.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'results':res})
    else:
        message = 'You have not searched any term'
        return render(request, 'search.html', {'message':message})


