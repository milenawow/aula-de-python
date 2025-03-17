#criar uma lista
lista =["macarrão","leite","nescau","biscoito","arroz"]
print(lista)
print("item :", lista[0])
lista =["macarrão","leite","nescau","biscoito","arroz"]
lista[0]= "feijao"

lista =["macarrão","leite","nescau","biscoito","arroz"]
print("Lista inicial: ", lista)
del lista[0]
print("Lista final: ", lista)

amigos = []
amigos.append("cabeção")
amigos.append("lula")
amigos.append("bolsonaro")
amigos.append("gilma")
print("lista de amigos :", amigos)

print("Lista de amigos :", amigos)
amigos.sort()
print("Lista de amigos ordenadas :", amigos)

lista = [10, 28, 6, 90, 67, 30, 49]

print(lista)
lista.append(79)
maiorElemento= max(lista)
menorElemento= min(lista)
print("Maior elemento da lista :", maiorElemento)
print("Menor elemento da lista :", menorElemento)

lista.sort(reverse=True)
print(lista)
      
lista = [10, 28, 6, 90, 67, 30, ] .append(30)
lista.append(80)
lista.append(30)
lista.append(10)
print(lista)
print("Elemento 3 é:", lista[3])


minhaTupla = ("André", "João", "Maria")
print(minhaTupla)

minhaTupla = ("André", "João", "Maria")
print("primeiro Elemento da tupla: ")


  lista: [10, 20, 30 ,40 , 50] # type: ignore