import time
#ele exportação da biblioteca time para manipular datas e horas, e para cronometrar programas. 
#random gera números aleatórios e selecionar elementos aleatoriamente de uma sequência
nome = input("Digite os nomes separados por virgula :").split(',')
mensagem_base = "olá, daqui uns minutos irei entrar em contato"
for nome in nome:
   nome = nome.strip()
   mensagem =mensagem_base.format(nome)
   print(mensagem)
   time.sleep(1)
