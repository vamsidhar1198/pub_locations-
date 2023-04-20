import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import os 

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")
data_path= os.path.join(dir_of_interest, "data","open_pubs1.csv")
data_path = data_path.replace("/..",'')
data = pd.read_csv(data_path)



st.header('Enter the longitude and latitude')
lati_min = data[['latitude','longitude']].min()[0]
long_min = data[['latitude','longitude']].min()[1]
lati_max = data[['latitude','longitude']].max()[0]
long_max = data[['latitude','longitude']].max()[1]
st.write('longitude min',long_min,'longitude max',long_max,'latitude min',lati_min,'latitude max',lati_max)
long = st.number_input('long')
lati = st.number_input('lati')

if st.button('SUBMIT'):
    
    locations = data[['latitude','longitude']].to_numpy()
    my_location = np.array([float(lati),float(long)])
    distances = np.sqrt(np.sum((locations-my_location)**2,axis=1))
    distances = distances.reshape(len(data),1)
    distance = np.hstack([locations,distances])
    data_sorted = distance[distance[:,2].argsort()]
    data_sorted = data_sorted[:5,:2]
    df = pd.DataFrame(data_sorted,columns=['lat','lon'])
    st.write(df)
    st.map(df)
else:
    pass
