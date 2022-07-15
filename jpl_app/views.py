import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import folium
import pandas as pd
import csv

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
    label = []
    dataset = []
    df_all = pd.read_csv("./jpl_app/static/InSAR_Data.csv")
    df_all = df_all.set_index([df_all.columns[0],df_all.columns[1]])
    df_all.fillna('NaN',inplace=True)

    lat = -119.299
    lon = 35.8852
    getRow = "Longitude == " + str(lat) + " and Latitude == " + str(lon)

    dataset_temp = df_all.query(getRow).values.tolist()
    dataset = sum(dataset_temp, [])
    label = df_all.columns.values.tolist()

    ma = folium.Map(location=[35.8831, -119.295], min_lat=34.0, max_lat=37.8,
               min_lon=-121.0, max_lon=-117.4, max_bounds=True, zoom_start=6, 
               min_zoom=6, max_zoom=10, width='%100', height='%100')
    # if there's an error about mouse position, then release comment-out
    # from folium.plugins import MousePosition
    # MousePosition().add_to(ma)
    ma.add_child(folium.LatLngPopup())
    ma = ma._repr_html_()

    context={
        'label': label,
        'dataset': dataset,
        'ma': ma,
    }
    return render(request, 'index.html', context)

