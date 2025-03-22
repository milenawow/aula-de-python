import pandas as pd

venda = pd.read_csv("Pasta1.csv")

resumo = venda.groupby("produto")["valor"].sum().reset_index()

with pd.ExcelWriter("relatorio.xlsx", engine="openpyxl") as writer:
    venda.to_excel(writer, sheet_name="Vendas", index=False)
    resumo.to_excel(writer, sheet_name="Resumo", index=False)

print("Relatório gerado com sucesso: relatorio.xlsx")