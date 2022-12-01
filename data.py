import pandas as pd
import streamlit as st
import numpy as np
#Título
st.title('Índices Soberanos 2010 - 2022')
st.subheader("Miembros del equipo")
st.markdown("""
- Palacios Ninahuanca, Ninoska
- Orozco Chupos, Frank
- Quispe Laura, Jhorch
- Parillo Sanchez, Yassmin Diana
""")
st.markdown("""
---
La información contenida en esta página web permite acceder al Dataset “Índices Soberanos 2010 - 2022” 
elaborado por el Ministerio de Economía y Finanzas del Perú.

Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/%C3%ADndices-soberanos-2010-2022)

---
""")

def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/data/indices_soberanos.csv"
    return pd.read_csv(url, sep= ',')
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()
st.write("**Datos generales**")
st.dataframe(df, use_container_width=st.session_state.use_container_width)
url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/data/indices_soberanos.csv"
c=pd.read_csv(url)

st.markdown("""**Comparación del INDICE_NOMINAL e INDICE_REAL**""") 
df = c.drop(columns = ["RENT_ANUAL_IN","RENT_ANUAL_IR"])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.write("**Gráfica**")
st.line_chart(c, x='FECHA', y=['INDICE_NOMINAL', 'INDICE_REAL'])

st.markdown("""INDICE_NOMINAL","RENT_ANUAL_IN""")
i1= c.drop(columns = ["FECHA","INDICE_REAL","RENT_ANUAL_IR"])
st.dataframe(i1, use_container_width=st.session_state.use_container_width)

st.markdown("""INDICE_NOMINAL","RENT_ANUAL_IN""")
i2= c.drop(columns = ["FECHA","INDICE_NOMINAL","RENT_ANUAL_IN"])
st.dataframe(i2, use_container_width=st.session_state.use_container_width)

st.markdown("""**Comparación del Renta Anual de Indice Nominal y Renta Anual Indice Real**""") 
df = c.drop(columns = ['INDICE_NOMINAL', 'INDICE_REAL'])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.write("**Gráfica**")
st.line_chart(c, x='FECHA', y=["RENT_ANUAL_IN","RENT_ANUAL_IR"])

df1= c
set_fecha= np.sort(df1["FECHA"].dropna().unique())
#Seleccion del departamento
opcion_fecha = st.selectbox('Selecciona una fecha', set_fecha)
df_fecha = df1[df1["FECHA"] == opcion_fecha]
num_filas = len(df_fecha.axes[0])
 


def load_fecha():
    url="https://raw.githubusercontent.com/Frank10OC/ejemplo/main/fecha.csv"
    return pd.read_csv(url, sep= ';')
dfecha = load_fecha()
st.write("**Fechas**")
st.dataframe(dfecha, use_container_width=st.session_state.use_container_width)
