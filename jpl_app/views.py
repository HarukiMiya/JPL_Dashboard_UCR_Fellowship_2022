from django.shortcuts import render
import folium
from .models import TimeSeriesData
from .vardata import lng_exist, lat_exist
from .utilities import LatLngPopupFix, binary_search
from folium import plugins
from folium.plugins import HeatMap
import pandas as pd

def chart(request):
    # latCenter and lngCenter are for keeping the current location of folium map
    latCenter = request.GET.get('latCenter')
    lngCenter = request.GET.get('lngCenter')
    if latCenter is None:
        latCenter = 35.8831
        lngCenter = -119.295
    else:
        latCenter = float(latCenter)
        lngCenter = float(lngCenter)
    center = [latCenter,lngCenter]

    zoomlevel = request.GET.get('zoomLevel')
    if zoomlevel is None:
        zoomlevel = 6
    else:
        zoomlevel = int(zoomlevel)
    
    strLat = request.GET.get('latVal')
    strLon = request.GET.get('lngVal')
    if not strLat is None:
        strLat = str(request.GET.get('latVal'))
        strLon = str(request.GET.get('lngVal'))
        # find the closest lat/lon
        strLat = str(binary_search(lat_exist, 0, 1748, float(strLat)))
        strLon = str(binary_search(lng_exist, 0, 1654, float(strLon)))
    time_series_list = TimeSeriesData.objects.filter(lon = strLon , lat = strLat).values_list()
    time_series_list = list(sum(time_series_list, ()))
    del time_series_list[:2]
    dataset = time_series_list
    dataset = ['NaN' if x==None else x for x in dataset]

    ma = folium.Map(location=center, min_lat=34.0, max_lat=37.8,
               min_lon=-121.0, max_lon=-117.4, max_bounds=True, zoom_start=zoomlevel, 
               min_zoom=6, max_zoom=10, width='%100', height='%100')

    # get lat/lon by clicking map and send them
    ma.add_child(LatLngPopupFix())

    if not strLat is None:
        folium.Marker(
            [float(strLat),float(strLon)], popup="Latitude: " + strLat + "<br>Longitude: " + strLon
        ).add_to(ma)

    df1 = pd.read_csv("./jpl_app/static/InSAR_20190122.csv")
    df_classification = pd.read_csv("./jpl_app/static/InSAR_classification.csv", usecols=[0,1,112])

    HeatMap(df1, min_opacity=.10, radius=5, blur=1 ).add_to(folium.FeatureGroup(name='Subsidence').add_to(ma))

    # blue area is non-change (val=1)
    # orange area is overall-increasing (val=2)
    # red area is overall-increasing (val=3)
    HeatMap(df_classification, min_opacity=.10, radius=1, blur=1 ).add_to(folium.FeatureGroup(name='Classification').add_to(ma))

    folium.LayerControl().add_to(ma)

    ma = ma._repr_html_()

    strNone = ""
    if all(i == 'NaN' for i in dataset):
        strNone = "No dataset is detected."
    else:
        strNone = "Dataset is detected."

    context={
        'strNone': strNone,
        'lat': strLat,
        'lng': strLon,
        'dataset': dataset,
        'ma': ma,
    }

    return render(request, 'index.html', context)

