quantidadeImpares = 0

quantidadesPares = 0

for i in range(5):
   numero = int(input("Informe um numero:  \n"))
   if numero % 2 == 0: # Numero é par
        quantidadesPares +=1 
   else:
       quantidadeImpares +=1
    
print(f"Quantidade de pares: {quantidadesPares}")
print(f"Quantidade de Impares: {quantidadeImpares}")

#Milena silva da costa
#Foram criadas duas variáveis, quantidadePares e quantidadeImpares. O laço de repetição vai pedir 5x para informar um número. Para cada número, o pograma vai verificar se o  mesmo é par. Se o número par é adicionado 1 á variavel quantidadePares. Se o número não é par, ele só pode ser ímpar. Nesse caso é adicionado 1 á variável quantidadeImpares. Ao final é mostrado os valores.
