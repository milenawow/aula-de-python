produto = {'Nome' : 'Feijão','quantidade':100}
nome = produto ['Nome']
quantidade = produto['quantidade']
print ("nome: ", nome)
print('quantidade :', quantidade)

#milena silva da costa
#primeiro ele pode dizer as informações, e se vc quiser dá para alterar o valor apenas mexendo no cem.


produto = {'nome': ['fejão', 'Arroz' , 'Farinha'], 'Quantidade': [10,10,100], 'preço' : [10,20,40]}
for nome, quantidade, preço in zip (produto['nome'],produto['Quantidade'], produto['preço']):
    print ("produto:", nome, "quantidade : " ,quantidade, "preço: ", preço, "reais")

#aqui ele adiciona o  valor

numeros = [1,2,3,3]

conjunto = set (numeros)

print(conjunto)
           
#aqui ele elimina o valor repetido

def imprimirNomeCurso() :
 print("curso de python")
imprimirNomeCurso()






