import gpxpy
import gpxpy.gpx


class GPXExporter:
    def __init__(self, coords, name="Parcours", description=""):
        self.coords = coords
        self.name = name
        self.description = description

    def to_gpx(self):
        gpx = gpxpy.gpx.GPX()
        gpx.name = self.name
        gpx.description = self.description

        track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(track)

        segment = gpxpy.gpx.GPXTrackSegment()
        track.segments.append(segment)

        for lon, lat in self.coords:
            segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon))

        return gpx.to_xml()

    def save(self, filename):
        xml = self.to_gpx()
        with open(filename, "w") as f:
            f.write(xml)
        return filename
