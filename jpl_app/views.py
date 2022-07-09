import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import folium


class IndexView(TemplateView):
    template_name = "index.html"

def index(request):
    # ma = folium.Map(location=[35.8831, -119.295], min_lat=34.1347, max_lat=37.6316,
    #            min_lon=-120.9486, max_lon=-117.6414, max_bounds=True, zoom_start=7, min_zoom=7, width=800, height=800)
    ma = folium.Map(location=[35.8831, -119.295], min_lat=34.0, max_lat=37.8,
               min_lon=-121.0, max_lon=-117.4, max_bounds=True, zoom_start=6, min_zoom=6, max_zoom=10, width='%100', height='%100')
    from folium.plugins import MousePosition
    MousePosition().add_to(ma)
    ma.add_child(folium.LatLngPopup())
    ma = ma._repr_html_()
    ctxt={
        'ma': ma
    }
    
    return render(request, 'index.html', ctxt)
