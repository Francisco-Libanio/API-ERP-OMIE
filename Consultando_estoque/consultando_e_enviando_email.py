import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

#Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('Arquivo com suas credenciais', scope)

#Autenticando 
gc = gspread.authorize(credentials)

#Abrindo a planilha
wks = gc.open_by_key('ID da planilha')

#Selecionando a primeira página da planilha
worksheet = wks.get_worksheet(0)

# Selecionando a primeira página da planilha
worksheet = wks.get_worksheet(0)

# Obtendo todos os valores das colunas 'Estoque' e 'Descrição', exceto a primeira linha
values_estoque = worksheet.col_values(7)[1:]  # Coluna 'Estoque'
values_descricao = worksheet.col_values(5)[1:]  # Coluna 'Descrição'
values_loja = worksheet.col_values(1)[1:]# coluna Familia
relatorio = []

# Iterando pelos valores das colunas 'Estoque', 'Descrição' e 'Loja'
for valor_estoque, descricao, loja in zip(values_estoque, values_descricao, values_loja):
    try:
        # Convertendo o valor para um número inteiro
        valor_int = int(valor_estoque)
        
        # Verificando as condições
        if valor_int < 5 and valor_int >= 0:
            lista_relatorio = [valor_estoque, descricao, loja]
            relatorio.append(lista_relatorio)
        elif valor_int < 0:
            lista_relatorio = [valor_estoque, descricao, loja]
            relatorio.append(lista_relatorio)
        # Se o valor for maior ou igual a 5, não faz nada
        
    except ValueError:
        # Ignorando valores que não puderem ser convertidos para número
        pass

# Criação do DataFrame após o loop for (fora do bloco try-except)
df_relatorio = pd.DataFrame(relatorio, columns=['quantidade', 'Descrição', 'Loja'])
display(df_relatorio)

#ESTE BLOCO DE CÓDIGO GARAVA TODO O DATAFRAME DE UMA VEZ 

#Importanto bibliotecas necessárias
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

#Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('arquivo com as credenciais.json', scope)

#Autenticando 
gc = gspread.authorize(credentials)

#Abrindo a planilha
wks = gc.open_by_key('coloque aqui o ID da sua planilha')


worksheet = wks.get_worksheet(0)
    

#Atualizando página
#worksheet.update_acell('a1','Funciona')
from gspread_dataframe import get_as_dataframe, set_with_dataframe


set_with_dataframe(worksheet, df_relatorio,include_index=False)

import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <h3><b>NESTE TEXTO VOCÊ PODE USAR CÓDIGO HTML</b></h3>"""
    
    msg = email.message.Message()
    msg['Subject'] = "Assunto do e-mail"
    msg['From'] = 'remetente'
    msg['To'] = 'destinatário'
    password = 'senha do aplicativo gmail' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()