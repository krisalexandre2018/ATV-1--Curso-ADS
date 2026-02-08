print('Bem Vindo ao sistema do Kristian Alexandre ')
valorBase = float(input('Digite o valor Base do plano:'))  # valor inicial do plano
idade = int(input('Informe a idade do cliente:'))          # idade do cliente
# Estrutura condicional para definir a porcentagem de aumento conforme a idade
if idade > 0 and idade < 19:
    porcentagem = 100
elif idade >= 19 and idade < 29:
    porcentagem = 150
elif idade >= 29 and idade < 39:
    porcentagem = 225
elif idade >= 39 and idade < 49:
    porcentagem = 240
elif idade >= 49 and idade < 59:
    porcentagem = 350
elif idade >= 59:
    porcentagem = 600
    
else:
    # Caso a idade seja inválida
    print('Idade inválida, reinicie o programa.')
    porcentagem = 0
# Só calcula se a porcentagem for válida
if porcentagem > 0:
    valorMensal = porcentagem * (valorBase / 100)  # cálculo do valor mensal
    print(f'Valor Mensal do plano é de: R$ {valorMensal:.2f}')  # saída formatada
