import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

#1. Título con diseño y animación
col1, col2, col3 = st.columns([1, 2, 1])  # Divide el espacio en 3 columnas

st.set_page_config(
    page_title="Agroindustria en Colombia",  # Título de la pestaña
    page_icon="🚜",  # Icono de la pestaña
    layout="wide" # Diseño ancho (opcional)
)

with col2:  # Columna central para el título
    st.markdown(
        """
        <style>
        .titulo {
            font-size: 3em;
            font-weight: bold;
            color: #336699;
            text-align: center;
            animation: color-change 5s infinite alternate;
        }
        @keyframes color-change {
            from { color: #336699; }
            to { color: #009933; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h1 class='titulo'>Agroindustria en Colombia</h1>", unsafe_allow_html=True)

#2. Imagen de encabezado
image = Image.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgQ-dfdJYD3InkuaFidnzuD5uNI9peoOk8DQ&s")
st.image(image, use_column_width=True)

