import streamlit as st
import pandas as pd
import random
from joblib import load
import numpy as np

model = load('model.joblib')

data = pd.read_csv('LucasSantos_FelipeSella_pre_processed_data.csv')

col1, col2, col3 = st.columns([0.18, 0.6, 0.1])

with col2:
    col1, col2, col3 = st.columns([0.21, 0.6, 0.1])
    with col2:
        st.image('DD-Logo.png', width=200)
    st.markdown("<h1 style='text-align: center;'>D & D Classificator</h1>", unsafe_allow_html=True)

    st.write("*Raças possíveis:* dragonborn, dwarf, elf, gnome, half-elf, half-orc, halfling, human, tiefling",)



col1, col2, col3 = st.columns([2, 2, 1])

with col2:
    speed = st.radio("Selecione o atributo speed:", (25, 30), horizontal=True)

min_height = 5
max_height = 500

min_weight = 5
max_weight = 500

height = st.slider(
    "Selecione a altura do personagem (inches):",
    min_value=min_height,
    max_value=max_height,
    value=min_height
)

weight = st.slider(
    "Selecione o peso do personagem (lbs):",
    min_value=min_weight,
    max_value=max_weight,
    value=min_weight
)

def classificar(values):    
    atributos_instancia = np.array([[height, weight, speed] + values])
    
    # Obtenha a classe prevista para essa instância
    classe_predita = model.predict(atributos_instancia)

    st.write(f"Classe prevista: {classe_predita[0]}")

def mostrar_texto():
    
    values = [random.randint(1, 20) for _ in range(6)]
    
    show_text = ""
    
    df = data.drop(['race', 'weight', 'height', 'speed'], axis=1)
    
    # st.write(values)
    
    for attr, value in zip(df.columns, values):

        show_text += f'{attr} : {value}; '
        
    st.write(show_text)
   
    classificar(values)

col1, col2, col3 = st.columns([0.34, 0.4, 0.1])

with col2:
    if st.button("Gerar Atributos"):
        mostrar_texto()
