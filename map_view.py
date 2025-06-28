import folium
from folium.plugins import Draw


def create_interactive_map(start_location=(48.8566, 2.3522), zoom_start=13):
    m = folium.Map(location=start_location, zoom_start=zoom_start)
    draw = Draw(
        draw_options={
            "polyline": True,
            "polygon": False,
            "circle": False,
            "rectangle": False,
            "marker": False,
            "circlemarker": False,
        },
        edit_options={"edit": False},
    )
    draw.add_to(m)
    return m


def extract_coordinates_from_draw(draw_data):
    """
    Extrait les coordonnées (lat, lon) du premier tracé
    de type LineString dans le champ 'all_drawings'.
    """
    coords = []

    if not draw_data:
        return coords

    drawings = draw_data.get("all_drawings", [])
    print(drawings)
    for feature in drawings:
        geometry = feature.get("geometry", {})
        if geometry.get("type") == "LineString":
            raw_coords = geometry.get("coordinates", [])
            # Conversion (lon, lat) -> (lat, lon)
            coords = [(lat, lon) for lon, lat in raw_coords]
            break  # On prend juste le premier tracé
    return coords
