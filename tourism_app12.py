import streamlit as st
import pandas as pd

# --- Load data ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('tourism_data.csv')  # Make sure the CSV has columns: State, City, Place, Latitude, Longitude
        return df
    except FileNotFoundError:
        st.error("Dataset file 'tourism_data.csv' not found. Please check the path.")
        return pd.DataFrame()

df = load_data()

# --- Recommendation function ---
def recommend_places(State=None, City=None, top_n=5):
    if df.empty:
        return pd.DataFrame()
    filtered = df.copy()

    if State:
        filtered = filtered[filtered['State'].str.lower() == State.lower()]
    if City:
        filtered = filtered[filtered['City'].str.lower() == City.lower()]

    return filtered.head(top_n)

# --- Streamlit UI ---
st.title("Tourism Place Recommendation")

st.write("You can enter a State, a City, or both to get recommended places.")

state_input = st.text_input("Enter State (optional)")
city_input = st.text_input("Enter City (optional)")
top_n = st.number_input("Number of places to recommend", min_value=1, max_value=20, value=5)

if st.button("Recommend"):
    results = recommend_places(State=state_input, City=city_input, top_n=top_n)
    
    if results.empty:
        st.warning("No matching places found.")
    else:
        st.dataframe(results)

        # --- Show map if coordinates exist ---
        if 'Latitude' in results.columns and 'Longitude' in results.columns:
            st.map(results[['Latitude', 'Longitude']])
        else:
            st.info("Latitude and Longitude not found in dataset. Map cannot be displayed.")
