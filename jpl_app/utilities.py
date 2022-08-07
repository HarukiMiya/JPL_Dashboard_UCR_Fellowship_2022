from branca.element import (MacroElement)
from jinja2 import Template

class LatLngPopupFix(MacroElement):
        """
        When one clicks on a Map that contains a LatLngPopup,
        a popup is shown that displays the latitude and longitude of the pointer.
        """
        _template = Template(u"""
                {% macro script(this, kwargs) %}
                    let latVal = 0.0000;
                    let lngVal = 0.0000;
                    let zoomLevel = 6;
                    let latCenter = 35.8831;
                    let lngCenter = -119.295;
                    var {{this.get_name()}} = L.popup();
                    function latLngPop(e) {
                            latVal = e.latlng.lat.toFixed(4);
                            lngVal = e.latlng.lng.toFixed(4);
                            latlngarr = [latVal,lngVal];
                            zoomLevel = {{this._parent.get_name()}}.getZoom();
                            latCenter = {{this._parent.get_name()}}.getCenter().lat.toFixed(4);
                            lngCenter = {{this._parent.get_name()}}.getCenter().lng.toFixed(4);
                    }
                    {{this._parent.get_name()}}.on('click', latLngPop).on('click', function(e){
                        $.ajax({
                            type: "get",
                            headers:{'X-CSRFToken':'{{ csrf_token }}'},
                            url: "http://127.0.0.1:8000",
                            data: { 'latVal': latVal, 'lngVal': lngVal, 'zoomLevel': zoomLevel, 'latCenter': latCenter, 'lngCenter': lngCenter },
                            success: function (response) {
                                parent.location.href = "?latVal="+latVal+"&lngVal="+lngVal+"&zoomLevel="+zoomLevel+"&latCenter="+latCenter+"&lngCenter="+lngCenter;
                                console.log("ajax in views success");
                            },
                            error: function (response) {
                                console.log("ajax in views fail")
                            },
                        })
                    });
                {% endmacro %}
                """)  # noqa

        def __init__(self):
            super(LatLngPopupFix, self).__init__()
            self._name = 'LatLngPopup'

def binary_search(arr, head, tail, x):
    if head <= tail:
        global mid
        mid = (head + tail) // 2 
        if arr[mid] == x:
            return x
        elif arr[mid] > x:
            return binary_search(arr, head, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, tail, x)
    else:
        return arr[mid]
