import os
import time

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.image('img/logo.png', width=100)

st.title('Reportes Universidad de Mexicali')

"""
Los gráficos son creados a partir de los archivos seleccionados
"""


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Selecciona un archivo', filenames)
    return os.path.join(folder_path, selected_filename)


filename = file_selector()
st.write('Ha seleccionado `%s`' % filename)

expense = pd.read_excel(filename, header=0,
                        sheet_name='Expenses Reports')

expense['Cantidad de gasto'] = expense['Cantidad de gasto'].str.replace(
    "$", "")

if st.checkbox('Mostrar datos del archivo'):
    expense

"""
## Gastos por categoría
"""

fig1 = px.pie(expense, values='Cantidad de gasto', names='Categoría', title='Gastos por categoría',
              color_discrete_sequence=px.colors.sequential.Rainbow)
fig1

"""
## Gastos por conceptos individuales
"""
fig2 = px.pie(expense, values='Cantidad de gasto', names='Título del gasto', title='Gastos por conceptos individuales',
              color_discrete_sequence=px.colors.sequential.Rainbow)
fig2


"""
## Gastos por fecha
"""

fig3 = px.pie(expense, values='Cantidad de gasto', names='Fecha', title='Gastos por fecha',
              color_discrete_sequence=px.colors.sequential.Rainbow)
fig3


fig4 = px.line(expense, x='Fecha', y='Cantidad de gasto',
               color='Título del gasto', line_shape='spline', render_mode='svg', template='plotly_white')
fig4

expander = st.beta_expander("FAQ")
expander.write(
    "1.- ¿Donde guardo los archivos? - Los archivos xls que se descargan del ERP deben ser guardados en la carpeta de este programa, y luego debe buscarse con el selector de archivos en esta página.")
expander.write(
    "2.- ¿Puedo modificar el archivo que guardé? - Aunque no es recomendable puede modificarse el contenido más no debe modificarse el nombre de la pestaña del archivo ni mover los datos de su posición original.")
expander.write(
    "3.- ¿Existe algún problema si renombro el archivo? - No lo hay, solo recuerde elegir el archivo renombrado con el selector de archivos y no modifique su extensión.")
expander.write(
    "4.- ¿Que extensiones soporta este sitio? - Este sitio soporta archivos con extensión xls, xlsx y xlsb, sin embargo no debe modificarse la extensión del archivo descargado desde el ERP.")
