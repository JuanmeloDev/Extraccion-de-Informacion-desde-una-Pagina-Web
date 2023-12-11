# -*- coding: utf-8 -*-
"""Extraccion_web.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iRvfm6DINqlIWulPSjmnYZPZPhZpI64H
"""

# Imports
import pandas as pd

url = 'https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonvpclatticeservices.html'

#Obtencion de la informacion.

table = pd.read_html(url)
Final_table = table[0]
Final_table.head()

# Filtrar la tabla.

table_1 = Final_table[['Actions', 'Description', 'Access level']]
table_2 = table_1.drop_duplicates(subset = ['Actions'])
table_2.head()
table_3 = table_2[table_2['Access level'] == 'Write']
table_3.head()

# Exportar tabla

table_3.to_excel('/content/drive/MyDrive/Informacion_Final/amazonvpclatticeservices.xlsx' , index = False)