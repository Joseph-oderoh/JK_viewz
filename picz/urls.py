from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.homepage, name='landing'),
    path('gallery/', views.gallery, name='gallery'),
    path('search/', views.search, name='search'),
    re_path('^location/(?P<locale>\w+)/$', views.location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
