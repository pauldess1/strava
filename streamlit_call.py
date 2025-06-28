import streamlit as st
from streamlit_folium import st_folium
from datetime import datetime
from map_view import create_interactive_map, extract_coordinates_from_draw


def streamlit_call():
    st.set_page_config(page_title="Traceur GPX", layout="wide")
    st.title("📍 Draw your run")

    # Entrées utilisateur
    name = st.text_input("Name", "Lunch Run")
    date = st.date_input("Choose the date")
    heure = st.time_input("Time")
    datetime_complet = datetime.combine(date, heure)
    st.write("Selected date and time :", datetime_complet.isoformat())

    # Carte
    map_obj = create_interactive_map()
    map_output = st_folium(
        map_obj, height=500, width=700, returned_objects=["all_drawings"]
    )
    coords = extract_coordinates_from_draw(map_output)

    if coords:
        st.success(f"{len(coords)} detected points.")

    return coords, name, datetime_complet
