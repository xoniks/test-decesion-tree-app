import streamlit as st
import joblib
import pandas as pd


st.title('Simple ML app for house price')

model_dt = joblib.load("models/iowa_model.pkl")
model_rf = joblib.load("models/iowa_model_rf.pkl")
features = joblib.load("iowa_features.pkl")

# ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

lot_area = st.number_input('Lot Area', value=8000)
year_built = st.number_input('Year Built', value=2000 )
first_floor_sf = st.number_input('1st Floor SF', value=800)
second_floor_sf = st.number_input('2nd Floor SF', value=800)
full_bath = st.number_input('Full Bath', value=2)
bedroom_above_gr = st.number_input('Bedroom Above Ground', value=3)
total_rooms_above_grd = st.number_input('Total Rooms Above Ground', value=6)

if st.button("Predict price with decession tree"):
    #transform this to df for predictions
    input_data_list = [lot_area, year_built, first_floor_sf, second_floor_sf, full_bath,
                    bedroom_above_gr, total_rooms_above_grd]
    input_df = pd.DataFrame([input_data_list] ,columns=features)
    prediction = model_dt.predict(input_df)[0]
    st.write(f"The predicted price is {prediction}")
    
if st.button("Predict price with decession random forest"):
    #transform this to df for predictions
    input_data_list = [lot_area, year_built, first_floor_sf, second_floor_sf, full_bath,
                    bedroom_above_gr, total_rooms_above_grd]
    input_df = pd.DataFrame([input_data_list] ,columns=features)
    prediction = model_rf.predict(input_df)[0]
    st.write(f"The predicted price is $ **{prediction}** ")