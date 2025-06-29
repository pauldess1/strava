from streamlit_call import streamlit_call
from trajectory_manager import TrajectoryManager
from datetime import time
from create_xml import GPX_Constructor

coords, name, dt, pace = streamlit_call()
start_time = time(hour=dt.hour, minute=dt.minute)
tm = TrajectoryManager(coords, pace, dt)
df = tm.output

gpx_constructor = GPX_Constructor(name, "running", df, dt)
gpx_constructor.generate_gpx()
