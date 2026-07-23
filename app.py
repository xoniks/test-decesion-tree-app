import streamlit as st
import joblib
import pandas


st.title('Simple ML app for house price')

model = joblib.load("iowa_model.pkl")
features = joblib.load("iowa_features.pkl")

# ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

lot_area = st.number_input('Lot Area', value=8000)
year_built = st.number_input('Year Built', value=2000 )
first_floor_sf = st.number_input('1st Floor SF', value=800)
second_floor_sf = st.number_input('2nd Floor SF', value=800)
full_bath = st.number_input('Full Bath', value=2)
bedroom_above_gr = st.number_input('Bedroom Above Ground', value=3)
total_rooms_above_grd = st.number_input('Total Rooms Above Ground', value=6)