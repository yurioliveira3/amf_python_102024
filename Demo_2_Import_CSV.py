import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('Demo_2_base_vendas.csv')

# Exibir as primeiras linhas para garantir que o arquivo foi carregado corretamente
print(df.head())

# Função para calcular o total de vendas
def calcular_vendas_totais(df):
    df['Total'] = df['Quantidade'] * df['Preço']
    total_vendas = df['Total'].sum()
    return total_vendas

# Função para encontrar o produto mais vendido
def produto_mais_vendido(df):
    produto_vendas = df.groupby('Produto')['Quantidade'].sum()
    mais_vendido = produto_vendas.idxmax()
    return mais_vendido

# Chamando as funções
print("Total de vendas: ", calcular_vendas_totais(df))
print("Produto mais vendido: ", produto_mais_vendido(df))