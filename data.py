import pandas as pd
import streamlit as st
import numpy as np
#color de pagina
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/vector-premium/fondo-oscuro-textura-tela_448617-61.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#####
col1, col2 = st.columns(2)

with col1:
   st.image("https://www.cayetano.edu.pe/cayetano/images/2018/Logo_Oficial.png", width=200)
  
with col2:
   st.image("https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/c5129789437667.5df458eb2c774.gif", width=200)

#####
#Título
st.markdown(f'<h1 style="color:#fafdfa;font-size:50px;">{"Índices Soberanos 2010 - 2022"}</h1>', unsafe_allow_html=True)
st.image("https://diariocorreo.pe/resizer/Fc7YLo9pXk9ykDycNAg8OkQ58LE=/580x330/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/KXKXRKMB7NGKLE3ASDKUGPVDRI.jpg", width=600)

st.markdown(f'<h1 style="color:#fafdfa;font-size:25px;">{"Miembros del equipo"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"- Palacios Ninahuanca, Ninoska"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"- Orozco Chupos, Frank"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"- Quispe Laura, Jhorch"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"- Parillo Sanchez, Yassmin Diana"}</h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"---"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"""La información contenida en esta página web permite acceder al Dataset “Índices Soberanos 2010 - 2022” 
elaborado por el Ministerio de Economía y Finanzas del Perú (MEF)."""}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/%C3%ADndices-soberanos-2010-2022)"}</h1>', unsafe_allow_html=True)
     
#IMPORTANDO DATOS
def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/indices_soberanos%20(1).csv"
    return pd.read_csv(url, sep= ',')
st.checkbox("Use container width", value=False, key="use_container_width")
st.markdown("""
---
""")

st.subheader("¿Qué son los Índices Soberanos?")
st.markdown("""
Es el conjunto de datos que replica el rendimiento de una crtera compuesta en su totaludad de bonos nominales
(o VAC) emitidos por el Tesoro que se encuentren vigentes, siendo la participacoión de cada tipo de bono en
la estructura del portafolio igual al valor de mercado de todos los bonos soberanos de ese tipo respecto al 
valor de mercado total de todos los bonos en soles nominales (o VAC) en circulación.
""")

###
st.subheader("Índice Nominal")
st.markdown("""
El índice nominal de una acción es el precio de una acción en el momento de constituir de una compañía.
""")
st.subheader("Índice Real")
st.markdown("""
El índice real es el precio de un bien, servicio o título en el mercado, teniendo en cuenta todos los elementos tangibles e intangibles que afectan al activo.
""")
st.subheader("Renta Anual")
st.markdown("""
La renta anual es la suma de todos los ingresos que ha recibido una persona a lo largo de un año tras restar aquellos gastos contemplados como deducibles.
""")
###



st.subheader("Datos")
df = load_data()
st.markdown("##### Datos Generales") 
st.dataframe(df, use_container_width=st.session_state.use_container_width)
url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/indices_soberanos%20(1).csv"
c=pd.read_csv(url)


##################################################################
#FECHAS
def load_fecha():
    url="https://raw.githubusercontent.com/Frank10OC/ejemplo/main/indices_soberanos_f.csv"
    return pd.read_csv(url, sep= ';')

dfecha = load_fecha()
#st.dataframe(dfecha, use_container_width=st.session_state.use_container_width)
#Filtraje de AÑO-MES-DÍA
st.markdown("##### Datos por filtro de fecha") 
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
   
#Respuesta del filtraje de fechas           
if (num_filas==1):
    col1, col2 = st.columns(2)
    with col1:
      st.markdown("###### Índice Nominal") 
      st.success(df_dia.iloc[0,3]) 
      st.markdown("###### Renta Anual de Índice Nominal ") 
      st.success(df_dia.iloc[0,4])
    with col2:
      st.markdown("###### Índice Real") 
      st.success(df_dia.iloc[0,5]) 
      st.markdown("###### Renta Anual de Índice Real") 
      st.success(df_dia.iloc[0,6])
else:
    st.error("No hay datos de la fecha") 

############################################################################


#st.markdown("""**Comparación del Índice Nominal e Índice Real**""")
st.subheader("Comparación del Índice Nominal e Índice Real")
df = c.drop(columns = ["RENTA ANUAL ÍNDICE NOMINAL","RENTA ANUAL ÍNDICE REAL"])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.write("**Gráfica: Índice Nominal - Índice Real**")
st.line_chart(c, x='FECHA', y=['ÍNDICE NOMINAL', 'ÍNDICE REAL'])

#st.markdown("""**Comparación de la Renta Anual de Índice Nominal y Renta Anual Índice Real**""")
st.subheader("Comparación de la Renta Anual de Índice Nominal y Renta Anual Índice Real")
df = c.drop(columns = ['ÍNDICE NOMINAL', 'ÍNDICE REAL'])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.write("**Gráfica: Renta Anual de Índice Nominal - Renta Anual de Índice Real**")
st.line_chart(c, x='FECHA', y=["RENTA ANUAL ÍNDICE NOMINAL","RENTA ANUAL ÍNDICE REAL"]) 





#### IMG ####
#from PIL import Image
#image = Image.open('Yass.jpg')
#st.image(image, caption='Sunrise by the mountains')
####
