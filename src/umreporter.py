import os
import time

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Reportes Universidad de Mexicali')

"""
Los gráficos son creados a partir de los archivos seleccionados
"""


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
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

# fig4 = px.line(expense, x='Cantidad de gasto', y='Fecha', color="Categoría", line_group="Categoria", hover_name="Categoría",
#         line_shape="spline", render_mode="svg")
# fig4 = px.line(expense, x='Fecha', y='Cantidad de gasto', color_discrete_sequence=px.colors.sequential.Rainbow)
fig4 = px.line(expense, x='Fecha', y='Cantidad de gasto',
               color='Título del gasto', line_shape='spline', render_mode='svg')

fig4

fig5 = px.bar(expense, x='Título del gasto', y='Cantidad de gasto')

fig5


left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write(
    "Here you could put in some really, really long explanations...")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'
