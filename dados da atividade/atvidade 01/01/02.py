import pandas as pd
from plyer import notification
vendas = pd.read_csv("vendas.csv", delimiter= ';')

indice = vendas['vvpp'].idxmax()

produto = vendas.loc[indice, 'produto']
quantidade = vendas.loc[indice, 'quantidade']
vendidos = vendas.loc[indice, 'vendidos']
vvpp = vendas.loc[indice, 'vvpp']

print(f'O produto {produto} é o mais vendido por produto, de {quantidade} unidades foi vendido {vendidos} unidades, com um lucro total de R${vvpp}')

notification.notify(
    title = 'Relatório',
    message = f'O produto {produto} é o mais vendido por produto, de {quantidade} unidades foi vendido {vendidos} unidades, com um lucro total de R${vvpp}',
    timeout = 20
)