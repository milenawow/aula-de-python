import time
import random

listaContato =[]
while True:
    listaContato.append(input("Digite os nomes"))
    maisnome = input("deseja continuar: ").lower()
    if maisnome == "n": 
        break
    def msg(lista):
        print(f"Boa noite {random.choice(lista)}")
        time.sleep(2)
        print("python")
        msg(listaContato)