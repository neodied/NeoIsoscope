class POI:
    def __init__(self, longitude, latitude, timeradius_min, alias=""):
        self.latitude = latitude
        self.longitude = longitude
        self.timeradius_min = int(timeradius_min)
        self.timeradius_sec = self.timeradius_min * 60
        self.latlong_str = f'{self.latitude},{self.longitude}'
        self.longlat_lst = [self.longitude, self.latitude]
        self.alias = alias


class IsolineKey:
    def __init__(self, center_lat, center_lon, radius_sec):
        self.center_lat = center_lat
        self.center_lon = center_lon
        self.radius_sec = radius_sec

    def __hash__(self):
        return hash((self.center_lat, self.center_lon, self.radius_sec))

    def __eq__(self, other):
        return (self.center_lat, self.center_lon, self.radius_sec) == (other.center_lat, other.center_lon, other.radius_sec)

    def __ne__(self, other):
        return not(self == other)


def serialize(obj):
    if isinstance(obj, IsolineKey):
        serial = f"{obj.center_lat} {obj.center_lon} {obj.radius_sec}"
        return serial
