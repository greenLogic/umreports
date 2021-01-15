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


def check_valid_file(filename):
    if filename.endswith('.xls'):
        print("Archivo aceptado")
    else:
        print("El archivo no tiene formato Excel")


def check_valid_file2(filename):
    if filename.endswith('.xls'):
        return "Archivo aceptado"
    else:
        return "El archivo no tiene formato Excel"


print(check_valid_file2(filename))

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
    "Here you could put in some really, really long explanations...")
