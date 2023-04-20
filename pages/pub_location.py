import streamlit as st
import pandas as pd
import numpy as np 
import os 

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

data_path = os.path.join(PARENT_DIR, "open_pubs1.csv")

data_path = data_path.replace("/..",'')
data = pd.read_csv(data_path)

local_authority= st.selectbox(
        'select the loacal authority',
        list(np.sort(data['local_authority'].unique())))


if st.button('local_authority'):
    loca1 = data[data['local_authority']==local_authority][['latitude','longitude']]
    st.map(loca1)


postal_code= st.selectbox(
    'select the loacal authority',
    list(np.sort(data['postcode'].unique())))


if st.button('postal_code'):
    post1 = data[data['postcode']==postal_code][['latitude','longitude']]
    st.map(post1)


