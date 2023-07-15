import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.title("Stress for  plastic strain of 0.2% Predictor")

C = st.number_input('C')
Si = st.number_input('Si')
Mn = st.number_input('Mn')
P = st.number_input('P')
S = st.number_input('S')
Ni = st.number_input('Ni')
Cr = st.number_input('Cr')
Mo = st.number_input('Mo')
Cu = st.number_input('Cu')
V = st.number_input('V')
Al = st.number_input('Al')
Temp = st.number_input('Temperature in Celsius')

if st.button('Predict'):
    
    query = np.array([C,Si,Mn,P,S,Ni,Cr,Mo,Cu,V,Al,Temp])
    query = query.reshape(1,12)
    
    st.title("0.2% Proof stress is " + str((pipe.predict(query)[0])))
