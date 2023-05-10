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
print(df['age'].describe()['mean'])
