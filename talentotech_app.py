import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import plotly.express as px
import datetime
#1. configuración inicial de la aplicación 
st.set_page_config(
  page_tityle="Dashboard Interactivo",
  page_icon="📊",
  layout="wide"
)
st.title("📊 Dashboard Interactivo con Streamlit")
st.sidebar.title("🔍 Ociones de navegación")
