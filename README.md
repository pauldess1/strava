# 🗺️ GPX Route Creator

A lightweight web app to **trace a custom route**, **generate synthetic running data**, and **export it as a `.gpx` file**. Built for athletes, developers, and Strava enthusiasts who want to simulate or prepare custom GPS routes.

---

## 🚀 Features

### 🌐 Interactive Web App (Streamlit + Folium)
- Draw a route directly on an interactive map.
- Input custom metadata: route name, description, etc.
- Visualize how many GPS points were captured.
- Export the route as a `.gpx` file with a single click.

### ⚙️ Synthetic Trajectory Generator
- Compute total distance based on GPS coordinates.
- Input your **pace** (`min/km`) and **start time**.
- Automatically generates a realistic timeline for the run.
- Interpolates GPS points over time to simulate motion.
- Output includes: latitude, longitude, timestamp.

### 📦 GPX Exporter
- Exports `.gpx` files compatible with platforms like **Strava**, **Garmin**, and **Komoot**.
- Ready for upload or further customization.

---

## 🧱 Project Structure
📁 project/
├── main.py # Streamlit app interface
├── map_view.py # Map creation & coordinate extraction
├── gpx_exporter.py # Handles GPX file generation
└──  trajectory_manager.py # Synthetic data generation

---

## 🧪 How it works

1. **Open the app** with `streamlit run main.py`.
2. **Draw your route** directly on the map.
3. **Enter metadata** like name, description, and pace.
4. **Generate a synthetic trajectory** using interpolation.
5. **Export the result as a .gpx file** and download it.

---

## 🔧 Tech Stack

- 🐍 Python 3.x
- 🗺️ [Streamlit](https://streamlit.io) — UI
- 📍 [Folium](https://python-visualization.github.io/folium/) — Map drawing
- 📏 [Geopy](https://geopy.readthedocs.io/) — GPS distance computation
- 📄 XML / GPX standard — For route export

---

## 📸 Preview

> *(Include a screenshot or GIF here to show the UI if available)*

---

## 💡 Use Cases

- Create simulated GPX tracks for **Strava uploads**
- Mock data generation for **fitness apps**
- Design custom running or cycling routes
- Prepare demo data for **machine learning models**

---

## ✅ Current State

✔ Route drawing  
✔ Coordinate extraction  
✔ Distance calculation  
✔ Trajectory generation  
✔ Export to `.gpx` file (basic version)

---

## 📌 TODO: Final Touches for Strava Integration

**Finish the V0 by creating the XML Generator:**

- [ ] Generate a proper GPX file containing:
  - Latitude
  - Longitude
  - Timestamp for each point
- [ ] Add required **metadata** (creator, time, route name, etc.)
- [ ] Build the interface to **collect metadata** and **run-specific info**
- [ ] (Optional) Extend GPX export with:
  - Heart rate
  - Cadence
  - Elevation
