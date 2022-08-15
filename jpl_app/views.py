from time import strptime
from django.shortcuts import render
import folium
from .models import GroundwaterData, PrecipitationData, TimeSeriesData
from .vardata import lng_exist, lat_exist, groundwater_lng_exist, groundwater_lat_exist, precipitation_lng_exist, precipitation_lat_exist
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
        strLat_ground = str(binary_search(groundwater_lat_exist, 0, 1349, float(strLat)))
        strLon_ground = str(binary_search(groundwater_lng_exist, 0, 1123, float(strLon)))
        strLat_precip = str(binary_search(precipitation_lat_exist, 0, 1349, float(strLat)))
        strLon_precip = str(binary_search(precipitation_lng_exist, 0, 1123, float(strLat)))
    
    time_series_list = TimeSeriesData.objects.filter(lon = strLon , lat = strLat).values_list()
    time_series_list = list(sum(time_series_list, ()))
    del time_series_list[:2]
    dataset = time_series_list
    dataset = ['NaN' if x==None else x for x in dataset]
    dataset_cols = [field.name for field in TimeSeriesData._meta.get_fields()]
    del dataset_cols[:2]
    for i in range(len(dataset_cols)):
        dataset_cols[i] = dataset_cols[i].split("_")[1:][0]

    groundwater_list = GroundwaterData.objects.filter(lon = strLon_ground , lat = strLat_ground).values_list()
    groundwater_list = list(sum(groundwater_list, ()))
    del groundwater_list[:2]
    dataset_groundwater = groundwater_list
    dataset_groundwater = ['NaN' if x==None else x for x in dataset_groundwater]
    groundwater_cols = [field.name for field in GroundwaterData._meta.get_fields()]
    del groundwater_cols[:2]
    for i in range(len(groundwater_cols)):
        groundwater_cols[i] = ''.join(groundwater_cols[i].split("_")[1:])

    precipitation_list = PrecipitationData.objects.filter(lon = strLon_precip , lat = strLat_precip).values_list()
    precipitation_list = list(sum(precipitation_list, ()))
    del precipitation_list[:2]
    dataset_precipitation = precipitation_list
    dataset_precipitation = ['NaN' if x==None else x for x in dataset_precipitation]
    precipitation_cols = [field.name for field in PrecipitationData._meta.get_fields()]
    del precipitation_cols[:2]
    for i in range(len(precipitation_cols)):
        precipitation_cols[i] = ''.join(precipitation_cols[i].split("_")[1:])
    print(precipitation_cols)
    print(dataset_precipitation)

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
    df_groundwater = pd.read_csv("./jpl_app/static/InSAR_groundwater.csv", usecols=[0,1,82])
    df_precipitation = pd.read_csv("./jpl_app/static/InSAR_precipitation.csv", usecols=[0,1,93])
    df_groundwater = df_groundwater[['Latitude', 'Longitude', '2018-10-30']]
    df_groundwater = df_groundwater.dropna()
    df_precipitation = df_precipitation[['Latitude', 'Longitude', '2019-01-22']]
    df_precipitation = df_precipitation.dropna()

    HeatMap(df1, min_opacity=.10, radius=5, blur=1 ).add_to(folium.FeatureGroup(name='Subsidence').add_to(ma))
    # blue area is non-change (val=1)
    # orange area is overall-increasing (val=2)
    # red area is overall-increasing (val=3)
    HeatMap(df_classification, min_opacity=.10, radius=1, blur=1 ).add_to(folium.FeatureGroup(name='Classification').add_to(ma))
    HeatMap(df_groundwater, min_opacity=.10, radius=3, blur=1 ).add_to(folium.FeatureGroup(name='Groundwater').add_to(ma))
    HeatMap(df_precipitation, min_opacity=.10, radius=2.5, blur=1 ).add_to(folium.FeatureGroup(name='Precipitation').add_to(ma))
    folium.LayerControl().add_to(ma)

    ma = ma._repr_html_()

    strNone = ""
    if all(i == 'NaN' for i in dataset):
        strNone = "No Subsidence is detected."
    else:
        strNone = "Subsidence is detected."
    strGr = ""
    if all(i == 'NaN' for i in dataset_groundwater):
        strGr = "No Groundwater is detected."
    else:
        strGr = "Groundwater is detected."
    strPr = ""
    if all(i == 'NaN' for i in dataset_precipitation):
        strPr = "No Precipitation is detected."
    else:
        strPr = "Precipitation is detected."

    context={
        'strNone': strNone,
        'strGr': strGr,
        'strPr': strPr,
        'lat': strLat,
        'lng': strLon,
        'dataset': dataset,
        'dataset_cols': dataset_cols,
        'groundwater': dataset_groundwater,
        'groundwater_cols': groundwater_cols,
        'precipitation': dataset_precipitation,
        'precipitation_cols': precipitation_cols,
        'ma': ma,
    }

    return render(request, 'index.html', context)

