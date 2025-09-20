!pip install streamlit
import streamlit as st
import pandas as pd
import streamlit as st

st.title('Tourism Recommendation system')

State = st.text_input('Enter State')
City = st.text_input('Enter City')
top_n = st.slider('Number of Recommendations', min_value=1, max_value=10, value=5)

if st.button('Recommend'):
    results = recommend_places(State=state, City=City, top_n=top_n)
    st.dataframe(results)
