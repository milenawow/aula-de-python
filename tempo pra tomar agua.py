import time
from win10toast import ToastNotifier

def lembrete_beber_agua(intervalo_minutoos=30):
    toaster= ToastNotifier()
    while True:
        toaster.show_toast(
        "bebe agua",
        "nao esqueça!",
         duration = 10
         )      
    time.sleep(intervalo_minutos*60)  
lembrete_beber_agua()
    