import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
data = pd.read_csv('Demo_1_GTA_inventario_cj.csv')

# Agrupar os dados por item, somando as quantidades e valores
grouped_data = data.groupby('item').sum()

# --- Gráfico de Pizza (quantidade por item) ---
plt.figure(figsize=(6, 6))
plt.pie(grouped_data['quantidade'], labels=grouped_data.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Quantidade por Item')

# --- Gráfico de Barras (valor total por item) ---
plt.figure(figsize=(8, 6))
plt.bar(grouped_data.index, grouped_data['valor'], color='skyblue')
plt.xlabel('Item')
plt.ylabel('Valor Total')
plt.title('Valor Total por Item')

# --- Gráfico de Linhas (quantidade e valor por item) ---
plt.figure(figsize=(8, 6))
plt.plot(grouped_data.index, grouped_data['quantidade'], marker='o', label='Quantidade', color='blue')
plt.plot(grouped_data.index, grouped_data['valor'], marker='s', label='Valor', color='green')
plt.xlabel('Item')
plt.ylabel('Quantidade / Valor')
plt.title('Quantidade e Valor por Item')
plt.legend()

# Mostrar todos os gráficos ao mesmo tempo
plt.show()
