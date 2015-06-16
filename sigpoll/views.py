from django.shortcuts import render
from django.http import HttpResponse

from sigpoll.models import LocationReport, Aircraft

import datetime as dt
import json


def json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


def aircraft_path(request, transponder):
    minute_ago = dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=30)
    q = LocationReport.objects.filter(aircraft_id=transponder, when__gte=minute_ago)
    return json_response({
        "type": "LineString",
        "coordinates": [[x.longitude, x.latitude] for x in q]
    })


def aircraft_location(request, transponder):
    aircraft = Aircraft.objects.get(id=transponder)
    lkp = aircraft.last_known_location
    return json_response({
        "type": "Feature",
        "geometry": {"type": "Point",
                     "coordinates": [lkp.longitude, lkp.latitude]},
        "properties": {"name": aircraft.name}
    })


def aircraft_visible(request):
    seen = Aircraft.active()

    return json_response({"aircraft": [
        {"id": x.id,
         "tail_number": "N-{}".format(x.tail_number)} for x in seen
    ]})


def home(request):
    return render(request, "sigpoll/web/home.html", {})
