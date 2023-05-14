# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import matplotlib as plt
import pandas as pd

st.title('app')

dataMt = pd.read_csv('sad-01-students-peformace - Math.csv')
dataPt = pd.read_csv('sad-01-students-peformace - Portuguese.csv')

df = pd.DataFrame(dataPt)
'''
print("dataPt")
print(df)
'''
escolaGP = df[df['school']=='GP']
'''
print("Alunos da escola GP")
print(escolaGP)
'''
print("Media das notas dos alunos da escola GP")
print(escolaGP['age'].mean())