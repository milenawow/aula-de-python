import pandas as pd
import matplotlib.pyplot as plt

vendas= pd.read_csv("vendas.csv", delimiter=";")


def determinar_cor(quantidade):
    if quantidade < 40:
        return "red" 
    elif 40 <= quantidade < 80:
        return "orange"  
    else:
        return "black" 

plt.figure(figsize=(8, 5))

cores = [determinar_cor(v) for v in vendas["vendido"]]
plt.bar(vendas["produto"], vendas["vendido"], color=cores)


plt.title("quantidade vendida por produto", fontsize=14)
plt.xlabel("produto")
plt.ylabel("quantidade vendida")
plt.xticks(rotation=45)  

plt.savefig("grafico.png", dpi=300, bbox_inches="tight")
plt.show()

print("✅ Gráfico gerado e salvo como 'grafico.png'")