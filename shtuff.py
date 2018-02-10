class POI:
    def __init__(self, longitude, latitude, timeradius_min, alias=""):
        self.latitude = latitude
        self.longitude = longitude
        self.timeradius_min = int(timeradius_min)
        self.timeradius_sec = self.timeradius_min * 60
        self.latlong_str = f'{self.latitude},{self.longitude}'
        self.longlat_lst = [self.longitude, self.latitude]
        self.alias = alias
