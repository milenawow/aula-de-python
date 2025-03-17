#coloquei meu nome em realse e pra isso criei essa função
def borda(s1):
    tam = len(s1)
    if tam:
        print('+','-'*tam,'+')
        print('I', 'Milena silva da costa','I')
        print('+','-'*tam,'+')
    print('Olá! Seja muito bem vindo(a) a lojinha de t-shirts da')
    borda('Milena Silva da Costa')
    print('promoção de t-shirts1!!! \n')
    # Criação das variáveis
    valor = float(input('Insira o valor da t-shirt: '))
    quantidade = int(input('Insira a quantidade de t-shirt: '))
    # Condição de desconto
    if quantidade < 10:
        desconto = 0
    elif quantidade < 20:
        desconto = 0.1
    else:
        desconto = 0.2
    #parametros para os valores
    valor_sem_desconto = quantidade * valor
    valor_com_desconto = valor * (1- desconto)
    valor_total = quantidade * valor_com_desconto
    valor_desconto =quantidade * valor * desconto
    porcentagem_desconto = desconto * 100
    #saida dos dados
    print(f'valor total sem desconto:', valor_sem_desconto)
    print(f'valor unitário R$ {valor: .2f}')
    print(f'valor com desconto: R$ {valor_total:.2f} ((porcentagem_desconto:.of)% de desconto)')
    print(f'valor total: R$ {valor_total:.2f} 9desconto total: R$ {valor_desconto:  .2f})')




    