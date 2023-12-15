#importanto biblioteca pra o print ficar mais organizado 
from pprint import pprint


#instalando biblioteca para gravar data frame no google sheets 
#!pip install gspread-dataframe

#instalando biblioteca de data 
#!pip install schedule

import os
import requests
from datetime import date
from dotenv import load_dotenv

class Omie:
    def __init__(self, empresa):
        
        self.AlterarPrecoItem = OmieAlterarPrecoItem(empresa)
        self.AlterarProduto = OmieAlterarProduto(empresa)
        self.ConsultarCliente = OmieConsultarCliente(empresa)
        self.ConsultarPedido = OmieConsultarPedido(empresa)
        self.ConsultarVendedor = OmieConsultarVendedor(empresa)
        self.ListarCenarios = OmieListarCenarios(empresa)
        self.ListarClientes = OmieListarClientes(empresa)
        self.ListarContasPagar = OmieListarContasPagar(empresa)
        self.ListarContasReceber = OmieListarContasReceber(empresa)
        self.ListarAnexo = OmieListarAnexo(empresa)
        self.ListarImpostosCenario = OmieListarImpostosCenario(empresa)
        self.ListarLocaisEstoque = OmieListarLocaisEstoque(empresa)
        self.ListarPedidos = OmieListarPedidos(empresa)
        self.ListarPosEstoque = OmieListarPosEstoque(empresa)
        self.ListarProdutos = OmieListarProdutos(empresa)
        self.ListarTabelaItens = OmieListarTabelaItens(empresa)
        self.ListarTabelasPreco = OmieListarTabelasPreco(empresa)
        self.ListarVendedores = OmieListarVendedores(empresa)
        self.ObterAnexo = OmieObterAnexo(empresa)
        self.PesquisarFamilias =OmiePesquisarFamilias(empresa)

class OmieAlterarPrecoItem:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/tabelaprecos/"
        self.call = "AlterarPrecoItem"
        self.nCodTabPreco = 0
        self.nCodProd = 0
        self.nValorTabela = 0

    def executar(self, console = True):
        return OmieApi().executar(self, self.empresa, console = console) 

class OmieAlterarProduto:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/produtos/"
        self.call = "AlterarProduto"
        self.codigo_produto = 0

    def executar(self, console = True):
        return OmieApi().executar(self, self.empresa, console = console) 

class OmieConsultarCliente:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/clientes/"
        self.call = "ConsultarCliente"
        self.codigo_cliente_omie = 0
        self.codigo_cliente_integracao = ""

    def executar(self):
        return OmieApi().executar(self, self.empresa) 

class OmieConsultarPedido:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/pedido/"
        self.call = "ConsultarPedido"
        self.codigo_pedido = 0

    def executar(self):
        return OmieApi().executar(self, self.empresa)

class OmieConsultarVendedor:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/vendedores/"
        self.call = "ConsultarVendedor"
        self.codigo = 0
        self.codInt = ""

    def executar(self):
        return OmieApi().executar(self, self.empresa)  
    
class OmieListarAnexo:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/anexo/"
        self.call = "ListarAnexo"
        self.nPagina = 1
        self.nRegPorPagina = 500
        self.nId = 0
        self.cTabela = ""

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console)

class OmieListarCenarios:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/cenarios/"
        self.call = 'ListarCenarios'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self):
        return OmieApi().executar(self, self.empresa) 

class OmieListarClientes:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/clientes/"
        self.call = 'ListarClientes'
        self.pagina = 1
        self.registros_por_pagina = 50

    def executar(self):
        return OmieApi().executar(self, self.empresa) 

    def todos(self):
        nome_lista_omie = "clientes_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            registros = self.executar()[nome_lista_omie]
            for registro in registros:
                lista.append(registro)
        return lista
    
class OmieListarContasPagar:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "financas/contapagar/"
        self.call = "ListarContasPagar"
        self.pagina = 1
        self.registros_por_pagina = 20

    def executar(self):
        return OmieApi().executar(self, self.empresa) 
    
    def todos(self):
        nome_lista_omie = "conta_pagar_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            registros = self.executar()[nome_lista_omie]
            for registro in registros:
                lista.append(registro)
        return lista
    
class OmieListarContasReceber:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "financas/contareceber/"
        self.call = "ListarContasReceber"
        self.pagina = 1
        self.registros_por_pagina = 20
        self.apenas_importado_api = "N"

    def executar(self):
        return OmieApi().executar(self, self.empresa) 
    
    def todos(self):
        nome_lista_omie = "conta_receber_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            registros = self.executar()[nome_lista_omie]
            for registro in registros:
                lista.append(registro)
        return lista

class OmieListarImpostosCenario:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/cenarios/"
        self.call = 'ListarImpostosCenario'
        self.consumo_final = "N"
        self.codigo_produto = 0       

    def executar(self):
        self.codigo_cliente_omie = OmieApi(self.empresa).cliente_imposto()
        self.codigo_cenario = OmieApi(self.empresa).cenario_imposto()
        return OmieApi().executar(self, self.empresa)

class OmieListarLocaisEstoque:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "estoque/local/"
        self.call = 'ListarLocaisEstoque'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self):
        return OmieApi().executar(self, self.empresa) 
    
class OmieListarPedidos:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/pedido/"
        self.call = "ListarPedidos"
        self.pagina = 1
        self.registros_por_pagina = 100
        self.apenas_importado_api = "N"

    def executar(self, console = False): 
        return OmieApi().executar(self, self.empresa, console = console)
    
    def todos(self, console = False):
        nome_lista_omie = "pedido_venda_produto"
        self.registros_por_pagina = 500
        consulta = self.executar(console = console)
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            lista_pagina = self.executar(console = console)[nome_lista_omie]
            for ind in lista_pagina:
                lista.append(ind)
        return lista
    
class OmiePesquisarFamilias:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/familias/"
        self.call = "PesquisarFamilias"
        self.pagina = 1
        self.registros_por_pagina = 100
        self.apenas_importado_api = "N"

    def executar(self, console = False): 
        return OmieApi().executar(self, self.empresa, console = console)
    
    def todos(self, console = False):
        nome_lista_omie = "famCadastro"
        self.registros_por_pagina = 500
        consulta = self.executar(console = console)
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            lista_pagina = self.executar(console = console)[nome_lista_omie]
            for ind in lista_pagina:
                lista.append(ind)
        return lista

class OmieListarPosEstoque:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "estoque/consulta/"
        self.call = 'ListarPosEstoque'
        self.nPagina = 1
        self.nRegPorPagina = 20
        self.dDataPosicao = date.today().strftime("%d/%m/%Y")
        self.cExibeTodos = "N"
        self.codigo_local_estoque = OmieApi(empresa).local_de_estoque()

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 

    def todos(self, console = False):
        nome_lista_omie = "produtos"
        self.nRegPorPagina = 500
        consulta = self.executar(console = console)
        total_de_paginas = consulta['nTotPaginas']
        lista = consulta[nome_lista_omie]
        while self.nPagina < total_de_paginas:
            self.nPagina += 1
            produtos = self.executar()[nome_lista_omie]
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarProdutos:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/produtos/"
        self.call = 'ListarProdutos'
        self.pagina = 1
        self.registros_por_pagina = 50
        self.apenas_importado_api = 'N'
        self.filtrar_apenas_omiepdv = 'N'

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console)

    def todos(self, console = False):
        nome_lista_omie = "produto_servico_cadastro"
        self.registros_por_pagina = 500
        consulta = self.executar(console = console)
        total_de_paginas = consulta['total_de_paginas']
        lista = consulta[nome_lista_omie]
        while self.pagina < total_de_paginas:
            self.pagina += 1
            produtos = self.executar(console = console)[nome_lista_omie]
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarTabelaItens:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/tabelaprecos/"
        self.call = 'ListarTabelaItens'
        self.nPagina = 1
        self.nRegPorPagina = 20
        self.nCodTabPreco = 0

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 

    def todos(self, console = False):
        nome_lista_omie = "listaTabelaPreco"
        self.nRegPorPagina = 500
        consulta = self.executar()
        total_de_paginas = consulta['nTotPaginas']
        lista = consulta[nome_lista_omie]['itensTabela']
        while self.nPagina < total_de_paginas:
            self.nPagina += 1
            busca = self.executar(console = console)
            produtos = busca[nome_lista_omie]['itensTabela']
            for produto in produtos:
                lista.append(produto)
        return lista

class OmieListarTabelasPreco:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "produtos/tabelaprecos/"
        self.call = 'ListarTabelasPreco'
        self.nPagina = 1
        self.nRegPorPagina = 20

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 
    
class OmieListarVendedores:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/vendedores/"
        self.call = "ListarVendedores"
        self.pagina = "1"
        self.registros_por_pagina = 100
        self.apenas_importado_api = "N"

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 
    
class OmieObterAnexo:
    def __init__(self, empresa):
        self.empresa = empresa
        self.caminho = "geral/anexo/"
        self.call = "ObterAnexo"
        self.cCodIntAnexo = "",
        self.cTabela = "",
        self.nId = 0,
        self.nIdAnexo = 0,
        self.cNomeArquivo = ""

    def executar(self, console = False):
        return OmieApi().executar(self, self.empresa, console = console) 

class OmieApi:
    def __init__(self, empresa = ""):
        self.caminho = ""
        self.call = ""
        load_dotenv()
        self.empresa = empresa

    def executar(self, metodo, empresa, console = False):

        self.empresa = empresa

        metodo_json = self.__converter_json(metodo)

        parametros = metodo_json.copy()
        parametros.pop('caminho')
        parametros.pop('call')
        parametros.pop('empresa')

        json_data = {}
        json_data['app_key'] = self.key()
        json_data['app_secret'] = self.secret()
        json_data['call'] = metodo_json['call']
        json_data['param'] = [parametros]
        response = requests.post('https://app.omie.com.br/api/v1/' + metodo_json['caminho'], json=json_data)
        if console == True: print(response.json())
        return response.json()

    def __converter_json(self, metodo):

        antigo = metodo.__dict__
        classe = metodo.__class__.__name__
        novo = {}

        for atributo in antigo:
            valor = antigo[atributo]
            atributo = atributo.replace("_" + classe + "__", "")
            atributo = atributo.replace("_" + classe + "_", "")
            atributo = atributo.replace("_" + classe, "") 
            novo[atributo] = valor     

        return novo

    def key(self): return os.getenv(self.empresa + '_KEY')
    def secret(self): return os.getenv(self.empresa + '_SECRET')
    def cliente_imposto(self): return os.getenv(self.empresa + '_CLIENTE_IMPOSTO')
    def cenario_imposto(self): return os.getenv(self.empresa + '_CENARIO_IMPOSTO')
    def local_de_estoque(self): return os.getenv(self.empresa + '_LOCAL_DE_ESTOQUE')

    #_______________________________________________________________

aplicativo_OMIE=['Empresa1','Empresa2','Empresa3','Empresa4','Empresa5']

#Consultando o código da familia dos produtos.
consulta = Omie('Empresa1').PesquisarFamilias
familias = consulta.todos()
#pprint(familias)

import pandas as pd

listagem = {
    'Empresa1': 'Código_da_familia1',
    'Empresa2': 'Código_da_familia2',
    'Empresa3': 'Código_da_familia3',
    'Empresa4': 'Código_da_familia4',
    'Empresa5': 'Código_da_familia5'
}

data_frames_produtos = {}

for loja, chave in listagem.items():
    produtos = []
    exemplo = Omie(loja).ListarProdutos
    exemplo.filtrar_apenas_familia = chave
    execucao = exemplo.todos()

    for produto in execucao:
        descricao_da_familia = produto['descricao_familia']
        codigo_do_produto = produto['codigo']
        marca = produto['marca']
        modelo = produto['modelo']
        qtd_estoque = produto['descricao']
        preco = produto['valor_unitario']

        produto_completo = (descricao_da_familia, codigo_do_produto, marca, modelo, qtd_estoque, preco)
        produtos.append(produto_completo)

    df_loja = pd.DataFrame(produtos, columns=['Descrição da familia', 'Código do produto', 'Marca', 'Modelo', 'Descrição', 'Preço'])
    data_frames_produtos[loja] = df_loja

# Agora data_frames é um dicionário onde cada chave é o nome da loja e o valor é o dataframe correspondente
# Por exemplo, para acessar o dataframe da loja 'App_Itapissuma':
for loja, df in data_frames_produtos.items():
    df['Código do produto'] = df['Código do produto'].astype(str)
    #print(f"Dataframe da loja: {loja}")
    #display(df)
    #print("\n")

lojas = ['Empresa1', 'Empresa2', 'Empresa3', 'Empresa4', 'Empresa5']
data_frames_estoque = []  # Lista para armazenar os dataframes de cada loja

for loja in lojas:
    exemplo = Omie(loja).ListarPosEstoque
    lista_estoque = exemplo.todos()
    
    estoque = []
    for i, c in enumerate(lista_estoque):
        codigo_do_produto = str(lista_estoque[i]['cCodigo'])
        qtd_estoque = lista_estoque[i]['nSaldo']
        preco = lista_estoque[i]['nPrecoUnitario']
        descricao = lista_estoque[i]['cDescricao']

        # Adicionando os dados na lista de estoque
        estoque_completo = [codigo_do_produto, qtd_estoque, preco, descricao]
        estoque.append(estoque_completo)

    # Criando o DataFrame a partir da lista de estoque específica da loja
    df_estoque_loja = pd.DataFrame(estoque, columns=['Código do produto', 'Estoque', 'Preço', 'Descrição'])
    df_estoque_loja['Total'] = df_estoque_loja['Preço'] * df_estoque_loja['Estoque']
    
    # Adicionando o dataframe da loja à lista de dataframes
    data_frames_estoque.append(df_estoque_loja)

# Exibindo os dataframes gerados para cada loja
for i, df_loja in enumerate(data_frames_estoque):
    nome_loja = lojas[i]
    #print(f"DataFrame da loja {nome_loja}:")
    #display(df_loja)
    #print("\n")

#ESTE BLOCO DE CÓDIGO GARAVA TODO O DATAFRAME DE UMA VEZ 

#Importanto bibliotecas necessárias
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

#Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('Coloque aqui suas credenciais .json', scope)

#Autenticando 
gc = gspread.authorize(credentials)

#Abrindo a planilha
wks = gc.open_by_key('Coloque aqui ID da planilha')

aba = 1
# Unindo os dataframes de produtos e estoque, respectivamente, um a um
for i in range(len(lojas)):
    loja_atual = lojas[i]
    df_produtos_loja = data_frames_produtos[loja_atual]
    df_estoque_loja = data_frames_estoque[i]
    
    # Unindo os dataframes com base nas colunas em comum ('Código do produto')
    df_merged = pd.merge(df_produtos_loja, df_estoque_loja, on='Código do produto', how='inner')
    
    #Selecionando a primeira página da planilha
    worksheet = wks.get_worksheet(aba)
    aba+=1

#Atualizando página
#worksheet.update_acell('a1','Funciona')
    from gspread_dataframe import get_as_dataframe, set_with_dataframe


    set_with_dataframe(worksheet, df_merged,include_index=False)