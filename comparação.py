import pandas as pd
import matplotlib.pyplot as plt

dados_produtos = pd.read_csv('produtos.csv', delimiter=';')

plt.figure(figsize=(10, 6))
for produto in dados_produtos['produto'].unique():
    dados_produtos = dados_produtos[dados_produtos['produto']==produto]
    plt.plot(dados_produtos['ano'], dados_produto['preco'], label=produto, marker='o')
plt.title('preco dos produtos ao longo dos anos')
plt.xlabel('ano')
plt.xlabel('preco')
plt.legend(title='produto')
plt.grid(true)
plt.show




