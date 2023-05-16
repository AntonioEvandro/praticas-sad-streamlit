# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import matplotlib as plt
import pandas as pd

#st.write("Texto armazenado")
#st.markdown('Isso é um texto.')

dataMt = pd.read_csv('sad-01-students-peformace - Math.csv')
dataPt = pd.read_csv('sad-01-students-peformace - Portuguese.csv')

df = pd.DataFrame(dataPt)

#print("dataPt")
#print(df)

def quebLinha():
    print("")

def questoes(num):
  if num == 1:
    escolaGP = df[df['school']=='GP']    #media = "{:.2f}".format(escolaGP['age'].mean())
    return st.write("%.2f é a media das notas dos alunos da escola GP" %escolaGP['age'].mean())
  elif num == 2:

    return 0
  elif num == 3:

    return 0
  elif num == 4:

    return 0
  elif num == 5:

    return 0
  elif num == 6:

    return 0
  elif num == 7:

    return 0
  elif num == 8:

    return 0
  elif num == 9:

    return 0
  elif num == 10:

    return 0
  else:
    return st.write("Questão não encontrada")

#num = int(input('Digite o número da questão que deseja ver o resultado'))
def input():
  num = st.number_input('Digite o número da questão', value=0, min_value=0, max_value=10)
  if num == 0:
    return st.write("Qual questão deseja ver o resultado?")
  else:
    st.write('Questão %i' %num)
  questoes(num)

st.title('app')

input()