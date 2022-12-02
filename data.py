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
#####
st.set_page_config(page_icon="📊", page_title="Detección de anomalías cardiacas", layout="wide")
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2FCayetano.Oficial%2F&psig=AOvVaw3lzMQmWUWh2iV5Dy4HHQ7Z&ust=1670074603736000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCICDy_GG2_sCFQAAAAAdAAAAABAD", width=200)
#####
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

st.markdown("""**Comparación del Renta Anual de Indice Nominal y Renta Anual Indice Real**""") 
df = c.drop(columns = ['INDICE_NOMINAL', 'INDICE_REAL'])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.write("**Gráfica**")
st.line_chart(c, x='FECHA', y=["RENT_ANUAL_IN","RENT_ANUAL_IR"]) 

#FECHAS
def load_fecha():
    url="https://raw.githubusercontent.com/Frank10OC/ejemplo/main/indices_soberanos_f.csv"
    return pd.read_csv(url, sep= ';')
dfecha = load_fecha()
st.write("**Fechas**")
st.dataframe(dfecha, use_container_width=st.session_state.use_container_width)

##################################################################33
#Sistema de filtros

#Construccion del set/list de AÑO (Valores unicos sin NA)
fecha_año = np.sort(dfecha['AÑO'].dropna().unique())
#Seleccion del AÑO
opcion_año = st.selectbox('Selecciona un año', fecha_año)
df_año = dfecha[dfecha['AÑO'] == opcion_año]
num_filas = len(df_año.axes[0]) 

#Construccion del set/list de MES (Valores unicos sin NA)
fecha_mes =(df_año['MES'].dropna().unique())
#Seleccion de MES
opcion_mes = st.selectbox('Selecciona un mes', fecha_mes)
df_mes = df_año[df_año['MES'] == opcion_mes]
num_filas = len(df_mes.axes[0]) 

#Construccion del set/list de distritos (Valores unicos sin NA)
fecha_dia = np.sort(df_año['DÍA'].dropna().unique())
#Seleccion del día
opcion_dia = st.selectbox('Selecciona un día', fecha_dia)
df_dia = df_mes[df_mes['DÍA'] == opcion_dia]
num_filas = len(df_dia.axes[0])
if (num_filas==1):
    st.markdown("###### INDICE NOMINAL") 
    st.success(df_dia.iloc[0,3])
    st.markdown("###### Renta Anual de Indice Nominal ") 
    st.success(df_dia.iloc[0,4]) 
    st.markdown("###### INDICE REAL") 
    st.success(df_dia.iloc[0,5]) 
    st.markdown("###### Renta Anual Indice Real") 
    st.success(df_dia.iloc[0,6])
else:
    st.error("No hay datos de la fecha") 
st.write('Numero de registros:', num_filas)
############################################################################

from PIL import Image
image = Image.open('Yass.jpg')

st.image(image, caption='Sunrise by the mountains')
