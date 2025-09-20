
import pandas as pd
import streamlit as st

st.title('Tourism Recommendation system')

State = st.text_input('Enter State')
City = st.text_input('Enter City')
top_n = st.slider('Number of Recommendations', min_value=1, max_value=10, value=5)

#Recommendation logic
def recommend_places(State, City, top_n):
    # Filter by state or city if provided
    filtered = df.copy()
    if State:
        filtered = filtered[filtered["State"].str.contains(State, case=False, na=False)]
    if City:
        filtered = filtered[filtered["City"].str.contains(City, case=False, na=False)]

    # If nothing matches, return top N from all
    if filtered.empty:
        return df.sample(top_n)
    else:
        return filtered.head(top_n)

if st.button('Recommend'):
    results = recommend_places(State=State, City=City, top_n=top_n)
    st.dataframe(results)
