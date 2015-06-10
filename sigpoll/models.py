from django.db import models
import datetime as dt


class CallsignReport(models.Model):
    callsign = models.CharField(max_length=8)
    when = models.DateTimeField()
    aircraft = models.ForeignKey('Aircraft', related_name='callsigns')

    def __repr__(self):
        return "<CallsignReport: callsign={} aircraft={}>".format(
            self.callsign,
            self.aircraft.name,
        )


class SquawkReport(models.Model):
    code = models.CharField(max_length=4)
    when = models.DateTimeField()
    aircraft = models.ForeignKey('Aircraft', related_name='squawks')

    def __repr__(self):
        return "<SquawkReport: code={} aircraft={}>".format(
            self.code,
            self.aircraft.name,
        )


class AltitudeReport(models.Model):
    altitude = models.IntegerField()
    when = models.DateTimeField()
    aircraft = models.ForeignKey('Aircraft', related_name='altitudes')

    def __repr__(self):
        return "<AltitudeReport: altitude={} aircraft={}>".format(
            self.altitude,
            self.aircraft.name,
        )


class HeadingReport(models.Model):
    speed = models.IntegerField()
    heading = models.IntegerField()
    when = models.DateTimeField()
    aircraft = models.ForeignKey('Aircraft', related_name='headings')

    def __repr__(self):
        return "<HeadingReport: speed={} heading={} aircraft={}>".format(
            self.speed,
            self.heading,
            self.aircraft.name,
        )


class LocationReport(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    ground = models.BooleanField()
    when = models.DateTimeField()
    aircraft = models.ForeignKey('Aircraft', related_name='locations')

    def __repr__(self):
        return "<LocationReport: lat={} lon={} aircraft={}>".format(
            self.latitude,
            self.longitude,
            self.aircraft.name,
        )


class Model(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    manufacturer = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    @property
    def make_and_model(self):
        return "{manufacturer} {name}".format(
            manufacturer=self.manufacturer,
            name=self.name,
        )

    def __repr__(self):
        return "<Model: {}>".format(self.make_and_model)


AIRCRAFT_TYPES = (
    ("1", "Glider"),
    ("2", "Balloon"),
    ("3", "Blimp/Dirigible"),
    ("4", "Fixed wing single engine"),
    ("5", "Fixed wing multi engine"),
    ("6", "Rotorcraft"),
    ("7", "Weight-shift-control"),
    ("8", "Powered Parachute"),
    ("9", "Gryroplane"),
)

AIRCRAFT_REGISTRANT_TYPE = (
    ("1", 'Individual'),
    ("2", 'Partnership'),
    ("3", 'Corporation'),
    ("4", 'Co-Owned'),
    ("5", 'Government'),
    ("8", 'Non Citizen Corporation'),
    ("9", 'Non Citizen Co-Owned'),
)


class Aircraft(models.Model):

    id = models.CharField(max_length=6, primary_key=True)
    model = models.ForeignKey('Model', null=True)
    tail_number = models.CharField(max_length=32, blank=True)

    type = models.CharField(max_length=4, choices=AIRCRAFT_TYPES)
    status = models.CharField(max_length=4)

    registrant_type = models.CharField(max_length=4, choices=AIRCRAFT_REGISTRANT_TYPE)
    registrant_name = models.TextField()
    registrant_street = models.TextField()
    registrant_street2 = models.TextField()
    registrant_city = models.TextField()
    registrant_state = models.TextField()
    registrant_zipcode = models.TextField()
    registrant_region = models.TextField()
    registrant_county = models.TextField()
    registrant_country = models.TextField()

    # LAST ACTION DATE
    # CERT ISSUE DATE
    # CERTIFICATION
    # FRACT OWNER
    # AIR WORTH DATE
    # EXPIRATION DATE

    @property
    def name(self):
        if self.tail_number:
            return "N{}".format(self.tail_number)
        return self.id

    @classmethod
    def active(self):
        minute_ago = dt.datetime.now() - dt.timedelta(seconds=30)
        return Aircraft.objects.filter(
            locations__when__gte=minute_ago
        ).distinct()

    @property
    def last_known_location(self):
        els = self.locations.order_by('-when')
        if els:
            return els[0]

    def __repr__(self):
        return "<Aircraft: {}>".format(self.name)
