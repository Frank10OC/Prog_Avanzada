import pandas as pd
import streamlit as st
import numpy as np
#####
col1, col2 = st.columns(2)

with col1:
   st.image("https://www.cayetano.edu.pe/cayetano/images/2018/Logo_Oficial.png", width=200)
  
with col2:
   st.image("https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/c5129789437667.5df458eb2c774.gif", width=200)

#####
#Título
st.title('Índices Soberanos 2010 - 2022')
st.image("https://diariocorreo.pe/resizer/Fc7YLo9pXk9ykDycNAg8OkQ58LE=/580x330/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/KXKXRKMB7NGKLE3ASDKUGPVDRI.jpg", width=600)

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
elaborado por el Ministerio de Economía y Finanzas del Perú (MEF).

Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/%C3%ADndices-soberanos-2010-2022)

---
""")

st.subheader("¿Qué son los Índices Soberanos?")
st.markdown("""
Es el conjunto de datos que replica el rendimiento de una crtera compuesta en su totaludad de bonos nominales
(o VAC) emitidos por el Tesoro que se encuentren vigentes, siendo la participacoión de cada tipo de bono en
la estructura del portafolio igual al valor de mercado de todos los bonos soberanos de ese tipo respecto al 
valor de mercado total de todos los bonos en soles nominales (o VAC) en circulación.
""")


#IMPORTANDO DATOS
def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/data/indices_soberanos.csv"
    return pd.read_csv(url, sep= ',')
#st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()
st.write("**Datos generales**")
st.dataframe(df, use_container_width=st.session_state.use_container_width)
url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/data/indices_soberanos.csv"
c=pd.read_csv(url)

st.markdown("""**Comparación del Índice Nominal e Índice Real**""") 
df = c.drop(columns = ["RENT_ANUAL_IN","RENT_ANUAL_IR"])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.write("**Gráfica: Comparación Índice Nominal - Comparación Índice Real**")
st.line_chart(c, x='FECHA', y=['INDICE NOMINAL', 'INDICE REAL'])

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
#Filtraje de AÑO-MES-DÍA
col1, col2, col3 = st.columns(3)

with col1:
   #Construccion del set/list de AÑO (Valores unicos sin NA)
   fecha_año = np.sort(dfecha['AÑO'].dropna().unique())
   #Seleccion del AÑO
   opcion_año = st.selectbox('Selecciona un año', fecha_año)
   df_año = dfecha[dfecha['AÑO'] == opcion_año]
   num_filas = len(df_año.axes[0]) 

with col2:
   #Construccion del set/list de MES (Valores unicos sin NA)
   fecha_mes =(df_año['MES'].dropna().unique())
   #Seleccion de MES
   opcion_mes = st.selectbox('Selecciona un mes', fecha_mes)
   df_mes = df_año[df_año['MES'] == opcion_mes]
   num_filas = len(df_mes.axes[0]) 
with col3:   
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

#### IMG ####
#from PIL import Image
#image = Image.open('Yass.jpg')
#st.image(image, caption='Sunrise by the mountains')
###
