import streamlit as st
from streamlit_folium import st_folium
from datetime import datetime
from map_view import create_interactive_map, extract_coordinates_from_draw


def streamlit_call():
    st.set_page_config(page_title="Traceur GPX", layout="wide")
    st.title("📍 Trace ton parcours et exporte en GPX")

    # Entrées utilisateur
    name = st.text_input("Nom du parcours", "Course du dimanche")
    date = st.date_input("Choisissez une date")
    heure = st.time_input("Choisissez une heure")
    datetime_complet = datetime.combine(date, heure)
    st.write("Date et heure sélectionnées :", datetime_complet.isoformat())

    # Carte
    map_obj = create_interactive_map()
    map_output = st_folium(
        map_obj, height=500, width=700, returned_objects=["all_drawings"]
    )
    coords = extract_coordinates_from_draw(map_output)

    if coords:
        st.success(f"{len(coords)} points détectés.")

    return coords, name, datetime_complet
