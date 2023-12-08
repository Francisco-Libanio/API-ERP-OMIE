from omie import Omie
from pprint import pprint
import schedule
import pandas as pd
import gspread


exemplo = Omie("EmpresaTeste").ListarProdutos

exemplo.registros_por_pagina = 50
exemplo.pagina = 1 

exec = exemplo.executar()

#exibindo o tipo da consulta 
print(type(exec['produto_servico_cadastro']))

#gravando os dados da consulta em uma variavel 
produto= exec['produto_servico_cadastro']

#Capturando o primeiro item da lista
produto = produto[0]
print(type(produto))
pprint(produto.keys())

produto= exec['produto_servico_cadastro']
#pprint(produto)

#Criando uma lista vazia que vai receber os dados capturados pelo for
produtos=[]
for i, c in enumerate(produto):
    
    #Capturando os dados das chaves.
    codigo_da_familia = produto[i]['codigo_familia']
    codigo_do_produto = produto[i]['codigo_produto']
    marca =  produto[i]['marca']
    modelo = produto[i]['modelo']
    qtd_estoque = produto[i]['quantidade_estoque']
    preco = produto[i]['valor_unitario']
    
    #Testando a captura de dados das chaves
    """
    print(f'Código da familia: {codigo_da_familia}')
    print(f'Código do produto: {codigo_do_produto}')
    print(f'Marca : {marca}')
    print(f'Modelo: {modelo}')
    print(f'Estoque: {qtd_estoque}')
    print(f'Preço: {preco}')
    print('-'*90)"""
    produto_completo = (codigo_da_familia, codigo_do_produto, marca, modelo, qtd_estoque, preco)
    produtos.append(produto_completo)

#Adicionando dados a um Data Frame  

print(type(produtos))
df_teste= pd.DataFrame(produtos,columns=['Código da familia', 'Código do produto','Marca','Modelo','Estoque','Preço'])
#df_teste
#display(df_teste)
#df_teste.info()
#df_teste.shape
print(produtos)


#Importanto bibliotecas necessárias
from oauth2client.service_account import ServiceAccountCredentials

#Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

#Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('Coloque aqui o OD da sua planilha', scope)

#Autenticando 
gc = gspread.authorize(credentials)

#Abrindo a planilha
wks = gc.open_by_key('Coloque aqui a sua chave ')

#Selecionando a primeira página da planilha
worksheet = wks.get_worksheet(0)

#Para testar a conexão use a linha a baixo
#worksheet.update_acell('a1','Funciona')
from gspread_dataframe import get_as_dataframe, set_with_dataframe


# Obter os valores da coluna A
column_a_values = worksheet.col_values(1)  # Coluna A é a primeira coluna (índice 1)

# Contar as linhas com células não vazias na coluna A
linhas_com_conteudo_na_coluna_a = sum(1 for cell in column_a_values if cell)

print(f'O número de linhas com conteúdo na coluna A é: {linhas_com_conteudo_na_coluna_a}')

# Adicionar o DataFrame abaixo da última linha com conteúdo na coluna A
linha_inicio_dataframe = linhas_com_conteudo_na_coluna_a + 1  # Linha após a última linha com conteúdo na coluna A

set_with_dataframe(worksheet, df_teste, row=linha_inicio_dataframe, include_index=False, include_column_header=False)
