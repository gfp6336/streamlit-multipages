import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Mapping Demo", page_icon="🌍")

st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write(
    "This demo shows how to use `st.map` to plot points on a map. "
    "The points are randomly generated around the city you choose."
)

CITIES = {
    "Sydney": (-33.8688, 151.2093),
    "Melbourne": (-37.8136, 144.9631),
    "Brisbane": (-27.4698, 153.0251),
}
city = st.selectbox("City", list(CITIES))
n_points = st.slider("Number of points", 100, 5000, 1000, step=100)
spread = st.slider("Spread (degrees)", 0.01, 0.5, 0.1)

lat, lon = CITIES[city]
rng = np.random.default_rng(42)
points = pd.DataFrame({
    "lat": lat + rng.normal(0, spread, n_points),
    "lon": lon + rng.normal(0, spread, n_points),
})
st.map(points)
