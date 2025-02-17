import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

# Título con diseño y animación
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
image = Image.open("https://encolombia.com/wp-content/uploads/2019/05/agroindustria-colombia.jpg")  # Reemplaza con la ruta de tu imagen
st.image(image, use_column_width=True)

