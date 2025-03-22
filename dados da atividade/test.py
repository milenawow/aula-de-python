import pandas as pd
from plyer import notification

df = pd.read_csv("Pasta1.csv")

df["total"] = df["quantidade"] * df["preco"]
total_vendas = df["total"].sum()

produto_mais_vendido = df.groupby("produto")["quantidade"].sum().idxmax()

mensagem = f"Resumo de Vendas:\nProduto mais vendido: {produto_mais_vendido}\nTotal de vendas: R$ {total_vendas:.2f}"

notification.notify(
    title="📊 Relatório de Vendas",
    message=mensagem,
    app_name="Automação de Vendas",
    timeout=10
)

print("\n✅ Notificação enviada com sucesso!")