# passo 1: importar base de dados

import pandas as pd
tabela = pd.read_csv("telecom_users.csv")

# passo 2: visualizar a base de dados
# entender as informações que você tem disponível
# para corrigir as cagadas da base de dados

# axis=0 -> linha, axis=1 -> coluna
tabela = tabela.drop("Unnamed: 0", axis=1) #excluir coluna ou linha tabela
tabela = tabela.drop("IDCliente", axis=1)

print(tabela)

# passo 3: tratamento de dados
# ver/ajustar qualquer valor que está sendo reconhecido de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # coerce = dexar nmr vazio quando der erro

# tratar valores vazios
# tratar colunas vazias --> excluir
# tabela = tabela.dropna(how="all"ou"any", axis=)

tabela = tabela.dropna(how="all", axis=1) # exclui coluna que tem todos os valores vazios
# tratar linhas com algum valor vazio -> excluir
tabela = tabela.dropna(how="any", axis=0)   # exclui linnha que tem algum valor vazios

print(tabela.info())
print(tabela)

# passo 4: análise simples -> entender como estão acontecendo os cancelamentos
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # map.... é pra formatar

# passo 5: análise mais completa
import plotly.express as px

# cria o gráfico
# para cada coluna da base de dados, criar um gráfico

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", color_discrete_sequence=["blue", "green"])
    # exibe o gráfico
    grafico.show()