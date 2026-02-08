# Função para exibir Boas-Vindas e o Cardápio da Pizzaria
def menuBoavindas():
    print('-' * 7, 'Bem Vindo a Pizzaria de Kristian Alexandre', '-' * 7)
    print('-' * 24, 'Cardápio', '-' * 24)
    print('-' * 3, '|', 'Tamanho', '|', 'Pizza Salgadas(PS)', '|', 'Pizza Doces(PD)', '|', '-' * 3)
    print('-' * 3, '|', '   P   ', '|', '     R$ 30,00     ', '|', '    R$34,00    ', '|', '-' * 3)
    print('-' * 3, '|', '   M   ', '|', '     R$ 45,00     ', '|', '    R$48,00    ', '|', '-' * 3)
    print('-' * 3, '|', '   G   ', '|', '     R$ 60,00     ', '|', '    R$66,00    ', '|', '-' * 3)
    print('-' * 58)
    return

# Exibe o cardápio uma vez
menuBoavindas()
# Variável acumuladora para o valor total do pedido
Total = 0
# Programa Principal
while True:  # Início do Loop
    # Entrada do sabor da pizza
    pizza = input('Entre com o sabor desejado (PS/PD): ').upper()
    if pizza == "PS" or pizza == "PD":  # Verifica se o sabor é válido
        tamanho = input('Digite o tamanho desejado (P, M, G): ').upper()

        if tamanho == "P" or tamanho == "M" or tamanho == "G":  # Verifica se o tamanho é válido
            # Incrementa o valor total baseado no sabor e tamanho
            if pizza == "PS" and tamanho == "P":
                Total += 30
                print('Você Pediu uma Pizza Salgada tamanho P: R$30,00')
            elif pizza == "PS" and tamanho == "M":
                Total += 45
                print(f'Você Pediu uma Pizza Doce tamanho M: R$45,00')
            elif pizza == "PS" and tamanho == "G":
                Total += 60
                print(f'Você Pediu uma Pizza Doce tamanho G: R$60,00')
            elif pizza == "PD" and tamanho == "P":
                Total += 34
                print(f'Você Pediu uma Pizza Doce tamanho P: R$34,00')
            elif pizza == "PD" and tamanho == "M":
                Total += 48
                print(f'Você Pediu uma Pizza Doce tamanho M: R$48,00')
            elif pizza == "PD" and tamanho == "G":
                Total += 66
                print(f'Você Pediu uma Pizza Doce tamanho G: R$66,00')
        else:
            print('Tamanho inválido. Tente novamente.')
            continue  # Volta ao início do loop
    else:
        print('Sabor inválido. Tente novamente.')
        continue  # Volta ao início do loop
    #Exibir Pizza Solicitada

    # Pergunta se o cliente deseja continuar pedindo
    continuar = input('Deseja pedir mais alguma coisa? (S/N): ').upper()
    if continuar == "S":
        continue  # Volta ao início do loop
    else:
        break  # Encerra o loop
# Exibe o valor total final
print(f'O valor total a ser pago é R$ {Total:.2f}')






