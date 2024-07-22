#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st
from nbconvert import NotebookExporter


# In[ ]:


st.title("Teste")
st.header("Seção 1:")
st.subheader("Subtítulo pra esse teste")


# In[ ]:


# Tirando do site os botões superior do Streamlit:

st.markdown("""
<style>
.st-emotion-cache-czk5ss.e16jpq800
{
    visibility:hidden;
}
.st-emotion-cache-zq5wmm.ezrtsby0
{
    visibility:hidden;
}
.st-emotion-cache-ztfqz8.ef3psqc5
{
    visibility:hidden;
}
<\style>
""", unsafe_allow_html=True)


# In[ ]:


st.markdown('''Mostrando um *texto*

            **aqui** mesmo''')


# In[ ]:


st.markdown("[Google Doodles](https://doodles.google/)")


# In[ ]:





# In[ ]:


# |exporti
 
nome = st.text_input("Diga seu nome")


# In[ ]:


option = st.radio("escolha uma opção:", options=["Masc","Fem"],index=1)


# In[ ]:


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


# In[ ]:


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


# In[ ]:


st.metric(label="Resultado de vendas", value=x, delta="-1.4 R$")


# In[ ]:


st.dataframe(map_data)


# In[ ]:





# In[ ]:





# In[ ]:


#!jupyter nbconvert --to script script1.ipynb

