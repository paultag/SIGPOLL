from .models import (CallsignReport, AltitudeReport, LocationReport,
                     HeadingReport, Aircraft, SquawkReport)

import datetime as dt
import pytz


HEADERS = (
    "message_type",
    "transmission_type",
    "session_id",
    "aircraft_id",
    "hex_ident",
    "flight_id",
    "date_generated",
    "time_generated",
    "date_logged",
    "time_logged",

    "callsign",
    "altitude",
    "ground_speed",
    "track",
    "latitude",
    "longitude",
    "vertical_rate",
    "squawk",
    "alert",
    "emergency",
    "spi",
    "on_ground",
)


def import_sbs(line, dedupe=False):
    els = []
    for el in sbs_to_db(line, dedupe=dedupe):
        if dedupe and el.is_dupe():
            continue
        el.save()
        els.append(el)
    return els


def sbs_to_db(line, dedupe=False):
    entry = dict(zip(HEADERS, line.strip().split(",")))
    yield from {
        'MSG': msg_to_db,
    }[entry['message_type']](entry, dedupe=dedupe)


def msg_to_db(data, dedupe=False):
    yield from {
        '1': msg_es_id_and_cat,
        '2': msg_es_surface_position,
        '3': msg_es_airborne_position,
        '4': msg_es_airborne_velocity,
        '5': msg_surveilance_alt,
        '6': msg_surveilance_id,
        # '7': disabled,
        '7': msg_air_to_air,
        '8': disabled,
    }[data['transmission_type']](data, dedupe=dedupe)


def payload_created_date(data, dedupe=False):
    when = dt.datetime.strptime(
        "{date_generated} {time_generated}".format(**data),
        # 2015/06/07 15:28:10.861
        "%Y/%m/%d %H:%M:%S.%f"
    )
    return pytz.timezone("America/New_York").localize(when)


def common(data):
    try:
        aircraft = Aircraft.objects.get(id=data['hex_ident'])
    except Aircraft.DoesNotExist:
        aircraft = Aircraft.objects.create(
            id=data['hex_ident'],
        )
    return {"aircraft": aircraft,
            "when": payload_created_date(data)}


def msg_es_id_and_cat(data, dedupe=False):
    yield CallsignReport(callsign=data['callsign'],
                         **common(data))


def msg_es_surface_position(data, dedupe=False):
    # has Alt, GS, trk, lat, long, grnd
    raise NotImplementedError("Not implented yet")


def msg_es_airborne_position(data, dedupe=False):
    # has alt, lat, long, alert, emerg, spi, ground
    if data['altitude']:
        yield AltitudeReport(altitude=int(data['altitude']), **common(data))
    yield LocationReport(latitude=float(data['latitude']),
                         longitude=float(data['longitude']),
                         ground=False,
                         **common(data))


def msg_es_airborne_velocity(data, dedupe=False):
    if data['ground_speed'] == '':
        return
    yield HeadingReport(speed=int(data['ground_speed']),
                        heading=int(data['track']),
                        **common(data))


def msg_surveilance_alt(data, dedupe=False):
    # alt, alert, spi, grnd
    if data['altitude']:
        yield AltitudeReport(altitude=int(data['altitude']), **common(data))


def msg_surveilance_id(data, dedupe=False):
    if data['squawk']:
        yield SquawkReport(code=data['squawk'], **common(data))


def msg_air_to_air(data, dedupe=False):
    # alt, ground
    if data['altitude'] == '':
        return
    yield AltitudeReport(altitude=int(data['altitude']), **common(data))


def disabled(data, dedupe=False):
    if False:
        yield
