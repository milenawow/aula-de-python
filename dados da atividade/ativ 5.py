import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv("vendas.csv")

resumo_vendas = df.groupby("produto")["quantidade"].sun().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x="produto", y="quantidade", data=resumo_vendas, palette="viridis")

plt.title("total de vendas por produto", fontsize=14)
plt.xlabel("produto")
plt.ylabel("quantidade vendida")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.savefig("grafico.png", dpi=300, bbox_inches="tight")
plt.show()

print("\n Grafico 'grafico.png' gerado com sucesso!")