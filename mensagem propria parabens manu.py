import pyautogui
import time

def enviar_mensagem(mensagem):
    time.sleep(3)  # Tempo para o usuário alternar para o WhatsApp Web
    pyautogui.typewrite(mensagem)
    pyautogui.press("enter")

def menu():
    print("Escolha o tipo de mensagem:")
    print("1 - Mensagem personalizada")
    
    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        mensagem = input("Digite sua mensagem personalizada: ")
    else:
        print("Opção inválida. Escolhendo mensagem padrão.")
        mensagem = "Olá! Esta é uma mensagem automática."

    
    return mensagem

if __name__ == "__main__":
    mensagem_escolhida = menu()
    print("Você tem 3 segundos para alternar para o wold...")
    enviar_mensagem(mensagem_escolhida)
    print("Mensagem enviada com sucesso!")
