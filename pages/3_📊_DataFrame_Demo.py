import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    "This demo shows how to use `st.dataframe` and `st.line_chart` with a "
    "multiselect filter. The numbers are synthetic, generated for this demo."
)


@st.cache_data
def make_data():
    rng = np.random.default_rng(7)
    regions = ["North", "South", "East", "West", "Central"]
    years = np.arange(2015, 2025)
    rows = []
    for r in regions:
        base = rng.uniform(50, 150)
        growth = rng.uniform(0.01, 0.08)
        for y in years:
            rows.append({"region": r, "year": int(y),
                         "sales": round(base * (1 + growth) ** (y - 2015) + rng.normal(0, 5), 1)})
    return pd.DataFrame(rows)


df = make_data()
chosen = st.multiselect("Regions", sorted(df["region"].unique()), default=["North", "South"])

if not chosen:
    st.error("Please select at least one region.")
else:
    sub = df[df["region"].isin(chosen)]
    st.write("### Sales by region", sub.sort_values(["region", "year"]))
    st.line_chart(sub.pivot(index="year", columns="region", values="sales"))
