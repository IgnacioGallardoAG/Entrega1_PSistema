# module name: helpers.py
import geopy.distance


class Distance:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def km(self):
        return geopy.distance.geodesic(
            ((self.source.__dict__())["latitude"],
             (self.source.__dict__()["longitude"])),
            ((self.destination.__dict__())["latitude"],
             (self.destination.__dict__()["longitude"]))
        ).km

    def nautical(self):
        return geopy.distance.geodesic(
            ((self.source.__dict__())["latitude"],
             (self.source.__dict__()["longitude"])),
            ((self.destination.__dict__())["latitude"],
             (self.destination.__dict__()["longitude"]))
        ).nautical
