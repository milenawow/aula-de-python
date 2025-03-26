import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('renda_desigualdade.csv')

# Exibir as primeiras linhas do DataFrame para ver a estrutura dos dados
print(df.head())

# Calculando a média de renda por gênero
media_renda_genero = df.groupby('sexo')['valor'].mean()

# Exibindo a média de renda por gênero
print("\nMédia de Renda por Gênero:")
print(media_renda_genero)

# Calculando a desigualdade de renda (diferença entre renda média de homens e mulheres)
desigualdade_renda = media_renda_genero['male'] - media_renda_genero['female']

print(f"\nDesigualdade de Renda entre Gêneros: {desigualdade_renda:.2f}")

# Gráfico de barras para visualização
media_renda_genero.plot(kind='bar', title='Média de Renda por Gênero', ylabel='Renda Média', xlabel='Gênero')


