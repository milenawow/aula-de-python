import time
#random gera números aleatórios e selecionar elementos aleatoriamente de uma sequência

from  win10toast import ToastNotifier

def lembret(intervalo_minutoos=30):
    toaster= ToastNotifier()
    while True:
        toaster.show_toast(
        "hora de  assistir anime",
        "nao esqueça!",
         duration = 10
         )      
    time.sleep(intervalo_minutos*60)  
lembret()
