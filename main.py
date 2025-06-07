import streamlit as st
from streamlit_folium import st_folium
from map_view import create_interactive_map, extract_coordinates_from_draw
from gpx_exporter import GPXExporter

st.set_page_config(page_title="Traceur GPX", layout="wide")
st.title("📍 Trace ton parcours et exporte en GPX")

# Entrées utilisateur
nom = st.text_input("Nom du parcours", "Course du dimanche")
description = st.text_area("Description", "Parcours pour Strava")

# Carte
map_obj = create_interactive_map()
map_output = st_folium(
    map_obj, height=500, width=700, returned_objects=["all_drawings"]
)
coords = extract_coordinates_from_draw(map_output)
print(coords)
coords = [
    (48.76179, 2.306828),
    (48.761451, 2.308116),
    (48.770955, 2.311807),
    (48.770333, 2.316484),
]

# Affichage
if coords:
    st.success(f"{len(coords)} points détectés.")

if st.button("📤 Exporter en GPX"):
    if coords:
        exporter = GPXExporter(coords, name=nom, description=description)
        file_path = exporter.save("parcours.gpx")

        with open(file_path, "rb") as f:
            st.download_button(
                label="📥 Télécharger le fichier GPX",
                data=f,
                file_name="parcours.gpx",
                mime="application/gpx+xml",
            )
    else:
        st.warning("Aucun parcours à exporter. Trace une ligne sur la carte.")
