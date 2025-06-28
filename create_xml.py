import xml.etree.ElementTree as ET


class GPX_Constructor:
    def __init__(self, name, type, data, time="2025-05-10T08:59:05Z"):
        self.name = name
        self.type = type
        self.time = time
        self.data = data

    def init_gpx(self):
        self.gpx = ET.Element(
            "gpx",
            xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
            xsi_schemaLocation="http://www.topografix.com/GPX/1/1 "
            "http://www.topografix.com/GPX/1/1/gpx.xsd "
            "http://www.garmin.com/xmlschemas/GpxExtensions/v3 "
            "http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd "
            "http://www.garmin.com/xmlschemas/TrackPointExtension/v1 "
            "http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd",
            creator="StravaGPX",
            version="1.1",
            xmlns="http://www.topografix.com/GPX/1/1",
            xmlns_gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1",
            xmlns_gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3",
        )
        metadata = ET.SubElement(self.gpx, "metadata")
        ET.SubElement(metadata, "time").text = self.time  # TODO: reformatting time


# TODO : Finish construction
# # Ajouter le segment de la track
# trk = ET.SubElement(gpx, 'trk')
# ET.SubElement(trk, 'name').text = '5kms samedi matin'
# ET.SubElement(trk, 'type').text = 'running'

# # Ajouter le trkseg (segment de track)
# trkseg = ET.SubElement(trk, 'trkseg')

# # Ajouter chaque point de track (trkpt) à partir de la DataFrame
# for idx, row in df.iterrows():
#     trkpt = ET.SubElement(trkseg, 'trkpt', lat=str(row['lat']), lon=str(row['lon']))
#     ET.SubElement(trkpt, 'ele').text = str(row['ele'])
#     ET.SubElement(trkpt, 'time').text = row['time']

#     # Ajouter les extensions pour chaque point de track
#     extensions = ET.SubElement(trkpt, 'extensions')
#     track_point_extension = ET.SubElement(extensions, 'gpxtpx:TrackPointExtension',
#     xmlns_gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1")
#     ET.SubElement(track_point_extension, 'gpxtpx:hr').text = str(row['hr'])
#     ET.SubElement(track_point_extension, 'gpxtpx:cad').text = str(row['cad'])

# # Créer l'arbre XML et écrire dans un fichier
# tree = ET.ElementTree(gpx)
# tree.write('output.gpx', encoding='UTF-8', xml_declaration=True)

# print("Le fichier XML a été généré avec succès.")
