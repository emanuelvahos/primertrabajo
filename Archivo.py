import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Título del dashboard
st.set_page_config(
  page_title="Agroindustria en Colombia",
  page_icon="🚜",
  
  layout="wide"
)

col1, col2, col3 = st.columns([1, 2, 1])  # Divide el espacio en 3 columnas

with col2:  # Columna central para el título
    st.markdown(
        """
        <style>
        .titulo {
            font-size: 3em;
            font-weight: bold;
            color: #336699; /* Un color azul llamativo */
            text-align: center;
            animation: color-change 5s infinite alternate; /* Animación de cambio de color */
        }
        @keyframes color-change {
            from { color: #336699; }
            to { color: #009933; } /* Cambia a un verde vibrante */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h1 class='titulo'>Agroindustria en Colombia</h1>", unsafe_allow_html=True)

# Imagen de encabezado (opcional)
image = Image.open("ruta_de_la_imagen.jpg")  # Reemplaza con la ruta de tu imagen
st.image(image, use_column_width=True)


# Generación de datos aleatorios
num_filas = 150
num_columnas = 8

# Genera nombres de columnas
nombres_columnas = [f"Variable_{i}" for i in range(num_columnas)]

# Crea el DataFrame con datos aleatorios
df = pd.DataFrame(np.random.rand(num_filas, num_columnas), columns=nombres_columnas)

# Selección de variables
st.sidebar.title("Selección de Variables")
variables_seleccionadas = st.sidebar.multiselect(
    "Selecciona las variables a mostrar", df.columns.tolist()
)

# Mostrar los datos seleccionados
if variables_seleccionadas:
    st.write("Datos de Agroindustria en Colombia:")
    st.dataframe(df[variables_seleccionadas])

    # Crear un gráfico de dispersión si se seleccionan al menos dos variables
    if len(variables_seleccionadas) >= 2:
        st.write("Gráfico de Dispersión:")

        # Permitir al usuario seleccionar las variables para el gráfico
        variable_x = st.selectbox("Variable para el eje X", variables_seleccionadas)
        variable_y = st.selectbox("Variable para el eje Y", variables_seleccionadas)

        fig, ax = plt.subplots()
        ax.scatter(df[variable_x], df[variable_y])
        ax.set_xlabel(variable_x)
        ax.set_ylabel(variable_y)
        st.pyplot(fig)

else:
    st.write("Selecciona al menos una variable para ver los datos.")


# Información adicional (opcional)
st.sidebar.markdown("### Información Adicional")
st.sidebar.write("Este dashboard muestra datos simulados de la agroindustria en Colombia.")
