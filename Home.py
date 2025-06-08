
import streamlit as st
import datetime



#Arquivos importantes para importar 

# Relatorio de Apontamento
# Relatorio de Faturamento
# Relatorio de Cadastro de itens (só quando necessário)
# Relatorio de OP Aberta
# Relatorio de pedidos em aberto

# Seria necessário importar para o banco ? 


st.header('Controle de consumo de combustivel')



hoje =  format(datetime.datetime.date)


st.write(hoje)