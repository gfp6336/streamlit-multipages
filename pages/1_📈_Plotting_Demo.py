import time

import numpy as np
import streamlit as st

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    "This demo shows how to use `st.line_chart` to show a chart that is "
    "animated as data streams in."
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
all_rows = last_rows
chart = st.empty()                    # redrawn each step: add_rows() was removed from recent Streamlit versions
chart.line_chart(all_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    all_rows = np.vstack([all_rows, new_rows])
    chart.line_chart(all_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically rerun the script when interacted with, so
# this button reruns the animation.
st.button("Re-run")
