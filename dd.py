# passo 1: importar base de dados

import pandas as pd
tabela = pd.read_csv("telecom_users.csv")

# passo 2: visualizar a base de dados
# entender as informações que você tem disponível
# para corrigir as cagadas da base de dados

# axis=0 -> linha, axis=1 -> coluna
tabela = tabela.drop("Unnamed: 0", axis=1) #excluir coluna ou linha tabela


display(tabela)