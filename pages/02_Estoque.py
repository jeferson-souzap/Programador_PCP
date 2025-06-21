import streamlit as st
from datetime import datetime
import os

import pandas as pd
import numpy as np



# Para conseguir o saldo de estoque PA
# Saldo = (Estoque inicial + apontamento ) - Faturamento

# Estrutura do saldo
# Estoque inicial (manual)
# Apontamento (entrada)
# Faturamento (Saidas)

#Configuração de pagina
st.set_page_config(page_title="Controle de estoque")
st.title("Sistema de controle de Estoque")


#Inicializando
if 'inventario_inicial' not in st.session_state:
    st.session_state.inventario_inicial = None

if 'apontamento' not in st.session_state:
    st.session_state.apontamento = None

if 'faturamento' not in st.session_state:
    st.session_state.faturamento = None


st.header('1. Carregar Arquivos')

