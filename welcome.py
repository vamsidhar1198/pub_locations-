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

st.header('WELCOME , DISCOVER THE _:red[PUBS]_ NEAR YOUR LOCATION 🍺')

value1 = st.slider(
    'Select a count of range of local authorities ',
    2, 680,(2,10),step=1) 
if st.button('local authority'):
    name1 = pd.DataFrame(data['local_authority'].value_counts())
    st.bar_chart(name1[(name1['local_authority']>value1[0]) &(name1['local_authority']<value1[1])])
else:pass

value2 = st.slider(
    'Select a count of range of pub name',
    1, 193,(1,10),step=1) 
if st.button('pub names'):
    name2 = pd.DataFrame(data['name'].value_counts())
    st.bar_chart(name2[(name2['name']>value2[0]) &(name2['name']<value2[1])])
else:pass
