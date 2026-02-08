# Função para escolher o tipo de madeira
def escolha_tipo():
    Madeiras = ['PIN', 'PER', 'MOG', 'IPE', 'IMB']
    print('Entre com um tipo de Madeira')
    print('PIN - Tora de Pinho')
    print('PER - Tora de Peroba')
    print('MOG - Tora de Mogno')
    print('IPE - Tora de Ipê')
    print('IMB - Tora de Imbuia')

    while True:
        def escolha_tipo():
            Madeiras = ['PIN', 'PER', 'MOG', 'IPE', 'IMB']
            print('Entre com um tipo de Madeira')
            print('PIN - Tora de Pinho')
            print('PER - Tora de Peroba')
            print('MOG - Tora de Mogno')
            print('IPE - Tora de Ipê')
            print('IMB - Tora de Imbuia')
        tipoMadeira = input('>> ').upper()  # converte para maiúsculo
        if tipoMadeira not in Madeiras:
            print('Escolha inválida, entre com o modelo novamente ')
            continue

        
        # Define o preço de acordo com a madeira escolhida
        if tipoMadeira == "PIN":
            valorMadeira = 150.40
        elif tipoMadeira == "PER":
            valorMadeira = 170.20
        elif tipoMadeira == "MOG":
            valorMadeira = 190.90
        elif tipoMadeira == "IPE":
            valorMadeira = 210.10
        elif tipoMadeira == "IMB":
            valorMadeira = 220.70

        return valorMadeira  # retorna o valor da madeira escolhida
# Função para escolher a quantidade de toras
def qtdToras():
    while True:
        try:
            qtd = int(input('Entre com a quantidade de toras (M³): '))
        except ValueError:  # se o usuário digitar algo que não seja número
            print("Erro: digite apenas números inteiros.")
            continue

        if qtd > 2000:
            print('Não aceitamos pedidos com essa quantidade de toras.Por Favor,entre com a quantidade novamente.')
            continue

        # Define o desconto de acordo com a quantidade
        if qtd < 100:
            desconto = 0
        elif 100 <= qtd < 500:
            desconto = 4 / 100
        elif 500 <= qtd < 1000:
            desconto = 9 / 100
        elif 1000 <= qtd <= 2000:
            desconto = 16 / 100

        return qtd, desconto  # retorna quantidade e desconto
# Função para escolher o transporte
def transporte():
    while True:
        print('Escolha o tipo de transporte')
        print('1 - Rodoviário (R$1000)')
        print('2 - Ferroviário (R$2000)')
        print('3 - Hidroviário (R$2500)')
        try:
            op = int(input('>> '))
        except ValueError:
            print("Erro: digite apenas números (1, 2 ou 3).")
            continue

        if op == 1:
            valorTransporte = 1000
        elif op == 2:
            valorTransporte = 2000
        elif op == 3:
            valorTransporte = 2500
        else:
            print("Opção inválida, tente novamente.")
            continue

        return valorTransporte  # retorna o valor do transporte escolhido
# PROGRAMA PRINCIPAL
print('Bem-vindo à Madeireira do Kristian Alexandre!')

valorMadeira = escolha_tipo()      # chama função da madeira
qtd, desconto = qtdToras()         # chama função da quantidade
valorTransporte = transporte()     # chama função do transporte

# Calcula o valor total
total = (valorMadeira * qtd) * (1 - desconto) + valorTransporte

# Exibe o resumo final do pedido
print(f'Total a pagar: R$ {total:.2f}')

