import pandas as pd
import streamlit as st
import numpy as np
#Título
st.title('Índices Soberanos 2010 - 2022')
st.subheader("Miembros del equipo")
st.markdown("""
- Palacios Ninahuanca, Ninoska
- Orozco Chupos, Frank
- Jorch
- Yasmin
""")
st.markdown("""
---
La información contenida en esta página web permite acceder al Dataset “Índices Soberanos 2010 - 2022” 
elaborado por el Ministerio de Economía y Finanzas del Perú. 
Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/%C3%ADndices-soberanos-2010-2022)
---
""")
def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/indices_soberanos%20(1).csv"
    return pd.read_csv(url)
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()
st.dataframe(df, use_container_width=st.session_state.use_container_width)
url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/indices_soberanos%20(1).csv"
c=pd.read_csv(url)
#comparación del Índice nominal e Índice real 
df = c.drop(columns = ["FECHA","INDICE_NOMINAL","INDICE_REAL"])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.line_chart(df)
#"INDICE_NOMINAL","RENT_ANUAL_IN"
i1= c.drop(columns = ["FECHA","INDICE_REAL","RENT_ANUAL_IR"])
st.dataframe(i1, use_container_width=st.session_state.use_container_width)
#"INDICE_NOMINAL","RENT_ANUAL_IN"
i2= c.drop(columns = ["FECHA","INDICE_NOMINAL","RENT_ANUAL_IN"])
st.dataframe(i2, use_container_width=st.session_state.use_container_width)

df1= c
set_fecha= np.sort(df1["FECHA"].dropna().unique())
#Seleccion del departamento
opcion_fecha = st.selectbox('Selecciona una fecha', set_fecha)
df_fecha = df1[df1["FECHA"] == opcion_fecha]
num_filas = len(df_fecha.axes[0])
 