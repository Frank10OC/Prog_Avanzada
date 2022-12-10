import pandas as pd
import streamlit as st
import numpy as np

#color de pagina
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://azasof.com/blog/wp-content/uploads/2018/03/000182241W.jpg");
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

st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Miembros del equipo"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"- Palacios Ninahuanca, Ninoska"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"- Orozco Chupos, Frank"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"- Quispe Laura, Jhorch"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"- Parillo Sanchez, Yassmin Diana"}</h1>', unsafe_allow_html=True)

st.markdown("---")
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"La información contenida en esta página web permite acceder al Dataset “Índices Soberanos 2010 - 2022” elaborado por el Ministerio de Economía y Finanzas del Perú (MEF)."""}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Fuente de datos: (https://www.datosabiertos.gob.pe/dataset/%C3%ADndices-soberanos-2010-2022)"}</h1>', unsafe_allow_html=True)
     
#IMPORTANDO DATOS
def load_data():
    url="https://raw.githubusercontent.com/Frank10OC/proyecto/main/indices_soberanos%20(1).csv"
    return pd.read_csv(url, sep= ',')
st.checkbox("Use container width", value=False, key="use_container_width")
st.markdown("""
---
""")
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"¿Qué son los Índices Soberanos?"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Los índices son números que reflejan la variación relativa de un precio o de un valor sobre un año base. En tanto, un índice soberano o índice de bono soberano es una medida consolidada del comportamiento observado de un grupo de bonos durante un determinado periodo. Es el conjunto de datos que replica el rendimiento de una cartera compuesta en su totalidad de bonos (o VAC) emitidos por el Tesoro que se encuentren vigentes, siendo la participación de cada tipo de bono en la estructura del portafolio igual al valor de mercado de todos los bonos soberanos de ese tipo respecto al valor de mercado total de todos los bonos en soles nominales (o VAC) en circulación."}</h1>', unsafe_allow_html=True)

###
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Índice Nominal"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"El índice nominal de una acción es el precio de una acción en el momento de constituir de una compañía."}</h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Índice Real"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"El índice real es el precio de un bien, servicio o título en el mercado, teniendo en cuenta todos los elementos tangibles e intangibles que afectan al activo."}</h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Renta Anual"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"La renta anual es la suma de todos los ingresos que ha recibido una persona a lo largo de un año tras restar aquellos gastos contemplados como deducibles."}</h1>', unsafe_allow_html=True)
###




st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Datos"}</h1>', unsafe_allow_html=True)
df = load_data()
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Datos Generales"}</h1>', unsafe_allow_html=True)
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

st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Datos por filtro de fecha"}</h1>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
   #Construccion del set/list de AÑO (Valores unicos sin NA)
   fecha_año = np.sort(dfecha['AÑO'].dropna().unique())
   #Seleccion del AÑO
   opcion_año = st.selectbox('Selecciona un año',fecha_año)
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
      st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Índice Nominal"}</h1>', unsafe_allow_html=True)          
      st.success(df_dia.iloc[0,3])
      st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Renta Anual de Índice Nominal"}</h1>', unsafe_allow_html=True)   
      st.success(df_dia.iloc[0,4])
    with col2:
      st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Índice Real"}</h1>', unsafe_allow_html=True)
      st.success(df_dia.iloc[0,5])
      st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Renta Anual de Índice Real"}</h1>', unsafe_allow_html=True)   
      st.success(df_dia.iloc[0,6])
else:
    st.error("No hay datos de la fecha")


############################################################################


st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Comparación del Índice Nominal e Índice Real"}</h1>', unsafe_allow_html=True)
df = c.drop(columns = ["RENTA ANUAL ÍNDICE NOMINAL","RENTA ANUAL ÍNDICE REAL"])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Gráfica: Índice Nominal - Índice Real"}</h1>', unsafe_allow_html=True)
st.line_chart(c, x='FECHA', y=['ÍNDICE NOMINAL', 'ÍNDICE REAL'])
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Cálculo del Índice del Tesoro Nominal"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Ponderaciones de los Bonos Elegibles"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"En cada fecha de rebalanceo, los bonos soberanos están sujetos a los criterios de elegibilidad. Una vez se determinen los bonos elegibles, se calculan las ponderaciones de cada uno de estos bonos dentro del Índice, estas ponderaciones son vigentes hasta la siguiente fecha de rebalanceo. Las ponderaciones son calculadas de la siguiente manera:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    W_{i;(f)} =
    \frac{Q_{i;(f)} . P_{i;(f)}}{\textstyle\sum_{i}^n \lbrack Q_{i;(f)} . P_{i;(f)} \rbrack}
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rendimiento Total Diario del Índice"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"El indicador de rendimiento es el rendimiento total diario, el cual considera los movimientos del precio de los valores dentro del Índice, las cobranzas de cupones y de amortizaciones. Es calculado de la siguiente manera:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    RTD_{(t)} =
    \Bigg[
    \frac{\textstyle\sum_{i}^n \lbrack Q_{i;(f)} . P_{i;(t)} + S_{i;(t)} \rbrack}{\textstyle\sum_{i}^n \lbrack Q_{i;(f)} . P_{i;(t-1)} + S_{i;(t-1)} \rbrack} -1 \Bigg]
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Valor del Índice"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"El valor del Índice es calculado diariamente de la siguiente manera:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    Valor del Índice_{(día t)} = Valor del Índice_{(día t-1)}*(1+RTP_{(t)}
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Cálculo del Índice del Tesoro Real"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rendimiento por precio"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Es el rendimiento obtenido por un bono debido a la variación de su precio sucio en el día t con respecto al día t-1, el cual es estimado así:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    Rendimiento por precio =
    \frac{Precio sucio_{t}-Precio sucio_{t-1}} {Precio sucio_{t-1}}
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rendimiento por cupón"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Es el rendimiento obtenido por un bono debido al pago de sus cupones en el día t, el cual es calculado así:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    Rendimiento por cupón =
    \frac{Cupón_{t}} {Precio_{t-1}}
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rendimiento por inflación"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Es el rendimiento obtenido debido a la variación del índice de reajuste diario en el día t con respecto al día t-1, el cual es calculado así:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    Rend. por inflación =
    \frac{Índice de reajuste diario_{t}-Índice de reajuste diario_{t-1}} {Índice de reajuste diario_{t-1}}
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rendimiento total"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Se obtiene a partir de la sumatoria, para cada bono, del rendimiento por precio, el rendimiento por cupón y el rendimiento por inflación generado."}</h1>', unsafe_allow_html=True)
st.latex(r'''
    Rendimiento total=
    Rend. por precio + Rend. por cupón + Rend. por inflación
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Saldo de caja"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Monto de efectivo generado a partir del pago de cupones recibidos por los tenedores en una fecha determinada."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Participación de cada bono en los índices"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Para el índice, la participación de cada bono es estimada así:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    p_{i} =
    \frac{VMB_{i_{(t)}}} {Saldo Caja_{(t)}+\textstyle\sum_{i=1}^n VMB_{i_{(t)}}}
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rendimiento total del índice"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Para el índice VAC, el rendimiento se obtiene así:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    RTP_{(t)} =
    \sum_{i=1}^N p_{i(t-1)} * RTB_{i(t)}
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Valor del Índice del Tesoro real"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Se obtiene así:"}</h1>', unsafe_allow_html=True)
st.latex(r'''
    Valor del Índice_{(t)} = Valor del Índice_{(t-1)}*(1+RTP_{(t)}
    ''')
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Comparación de la Renta Anual de Índice Nominal y Renta Anual Índice Real"}</h1>', unsafe_allow_html=True)
df = c.drop(columns = ["ÍNDICE NOMINAL", "ÍNDICE REAL"])
st.dataframe(df, use_container_width=st.session_state.use_container_width)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Gráfica: Renta Anual de Índice Nominal - Renta Anual de Índice Real"}</h1>', unsafe_allow_html=True)
st.line_chart(c, x='FECHA', y=["RENTA ANUAL ÍNDICE NOMINAL","RENTA ANUAL ÍNDICE REAL"])
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Impuesto a la Renta (IR)"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"El impuesto a la renta es un tributo que se determina anualmente, tiene vigencia del 01 de enero al 31 de diciembre."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rentas de Capital - Primera Categoría:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Generadas por el arrendamiento, subarrendamiento o cualquier tipo de cesión de bienes muebles o inmuebles. El pago debes hacerlo tú mismo y corresponde al 6.25% sobre la renta neta (equivalente al 5% sobre la renta bruta)."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Cálculo del impuesto a la renta de quinta categoría:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"1. Identifica el monto"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"2. Aplica el impuesto"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"3. Comparael impuesto"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rentas de Capital - Segunda Categoría:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Corresponde a venta de acciones o valores mobiliarios, intereses por colocación de capitales, regalías, patentes, rentas vitalicias, derechos de llave y otros."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Cálculo del impuesto a la renta de segunda categoría por venta de inmuebles:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"1. Determina el costo de adquisición actualizado de tu inmueble"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"2. Determinar la Renta Neta"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"3. Determinación del impuesto"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rentas del Trabajo - Cuarta Categoría:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Corresponden a servicios prestados de manera independiente de cualquier profesión, ciencia, arte u oficio. También, están aquí los trabajadores del Estado con contrato CAS, los directores, consejeros regionales y regidores municipales. Si estos ingresos se complementan con actividades empresariales o viceversa, el total de la renta que se obtenga se considerará como renta de Tercera Categoría es decir una renta empresarial."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Cálculo del impuesto a la renta de cuarta categoría:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"1. Descuenta el 20% de los ingresos percibidos o cobrados durante el año"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"2. Descuenta el valor de 7 UIT"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"3. Aplica la tasa del impuesto por cada tramo de ingresos"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rentas del Trabajo - Quinta Categoría:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Son los ingresos obtenidos por el trabajo personal prestado en relación de dependencia (planilla), incluidos cargos públicos, tales como sueldos, salarios, asignaciones, gratificaciones, bonificaciones, aguinaldos, comisiones, compensaciones en dinero o en especie, gastos de representación y, en general, toda retribución por servicios personales."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Cálculo del impuesto a la renta de quinta categoría:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"1. Suma tus ingresos totales del año y descuéntale 7 UIT"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"2. Descuenta (en caso tengas), el monto de tus gastos deducibles del año (máximo 3 UIT)"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"3. Aplica la tasa del impuesto por cada tramo de ingresos"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Descuenta las retenciones que tu empleador realizó durante el año"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Rentas de Fuente Extranjera:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Provienen de una fuente ubicada fuera del territorio nacional. No se categorizan y se consideran para efectos del Impuesto, siempre que se hayan percibido. Por ejemplo, la renta obtenida por alquilar un inmueble en el extranjero, los intereses obtenidos por certificados de depósitos bancarios de entidades financieras del exterior, la renta obtenida por prestar servicios en el exterior, entre otras."}</h1>', unsafe_allow_html=True)

st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")

col1, col2 = st.columns(2)
with col1:
   st.image("https://facien.cayetano.edu.pe/images/documentacion/noticias/logos/logotipo_Ciencias.png", width=200)
with col2:
   st.image("https://www.cayetano.edu.pe/cayetano/images/2020/ingenieria-ambiental/TIT.png", width=200)
    
         
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Colaboradores:"}</h1>', unsafe_allow_html=True)
col1, col2, col3, col4= st.columns(4)
with col1:
   st.image("Nino.jpg", width=150)
   st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Palacios Ninahuanca, Ninoska"}</h1>', unsafe_allow_html=True)
with col2:
   st.image("Frank.jpg" , width=150)
   st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Orozco Chupos, Frank"}</h1>', unsafe_allow_html=True)
with col3:   
   st.image("Jhorch.jpg", width=150)
   st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Quispe Laura, Jhorch"}</h1>', unsafe_allow_html=True)
with col4:
   st.image("Yass.jpg" , width=150)
   st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Parillo Sánchez, Yassmin"}</h1>', unsafe_allow_html=True)  
  


st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Curso:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Programación Avanzada - 2022-2"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:20px;">{"Profesor:"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Montalvo García, Peter"}</h1>', unsafe_allow_html=True)
