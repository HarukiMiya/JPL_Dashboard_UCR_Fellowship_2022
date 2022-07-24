import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import folium
from .models import TimeSeriesData


class IndexView(TemplateView):
    template_name = "index.html"

def index(request):
    ma = folium.Map(location=[35.8831, -119.295], min_lat=34.0, max_lat=37.8,
               min_lon=-121.0, max_lon=-117.4, max_bounds=True, zoom_start=6, min_zoom=6, 
               max_zoom=10, width='%100', height='%100')
    # if there's an error about mouse position, then release comment-out
    # from folium.plugins import MousePosition
    # MousePosition().add_to(ma)
    ma.add_child(folium.LatLngPopup())
    ma = ma._repr_html_()
    ctxt={
        'ma': ma
    }
    return render(request, 'index.html', ctxt)

def chart(request):
    intLon = -117.6414
    intLat = 37.6256
    time_series_list = TimeSeriesData.objects.filter(lon = str(intLon) , lat = str(intLat)).values_list()
    time_series_list = list(sum(time_series_list, ()))
    del time_series_list[:2]
    dataset = time_series_list
    dataset = ['NaN' if x==None else x for x in dataset]

    ma = folium.Map(location=[35.8831, -119.295], min_lat=34.0, max_lat=37.8,
               min_lon=-121.0, max_lon=-117.4, max_bounds=True, zoom_start=6, 
               min_zoom=6, max_zoom=10, width='%100', height='%100')
    # if there's an error about mouse position, then release comment-out
    # from folium.plugins import MousePosition
    # MousePosition().add_to(ma)
    ma.add_child(folium.LatLngPopup())
    ma = ma._repr_html_()

    context={
        'dataset': dataset,
        'ma': ma,
    }

    return render(request, 'index.html', context)

