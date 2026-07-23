import streamlit as st
import joblib
import pandas


st.title('Simple ML app for house price')

model = joblib.load("iowa_model.pkl")
features = joblib.load("iowa_features.pkl")


