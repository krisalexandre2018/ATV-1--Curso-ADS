# Mensagem de boas-vindas com nome completo
print('=' * 60)
print('Bem-vindo à Lista de Contatos de Kristian Alexandre')
print('=' * 60)

# Inicialização da lista de contatos e id_global
lista_contatos = []
id_global = 5569820


# Função para cadastrar contato
def cadastrar_contato(id):
    """Função que cadastra um novo contato no sistema"""
    print('-' * 50)
    print('---------- MENU CADASTRAR CONTATO ----------')
    print(f'Id do Contato: {id}')

    # Solicitando dados do contato
    nome = input('Por favor entre com o nome do Contato: ')
    atividade = input('Por favor entre com a Atividade do contato: ')
    telefone = input('Por favor entre com o telefone do contato: ')

    # Criando dicionário com os dados do contato
    contato = {
        'id': id,
        'nome': nome,
        'atividade': atividade,
        'telefone': telefone
    }

    #Adicionando o contato na lista
    lista_contatos.append(contato.copy())
    print('Contato cadastrado com sucesso!')
    print('-' * 50)


#Função para consultar contatos
def consultar_contatos():
    """Função que permite consultar contatos de diferentes formas"""
    while True:
        print('-' * 50)
        print('---------- MENU CONSULTAR CONTATO ----------')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos')
        print('2 - Consultar por Id')
        print('3 - Consultar por Atividade')
        print('4 - Retornar ao menu')
        opcao = input('>> ')

        #Consultar Todos
        if opcao == '1':
            print('-' * 50)
            print('---------- TODOS OS CONTATOS ----------')
            if len(lista_contatos) == 0:
                print('Nenhum contato cadastrado.')
            else:
                for contato in lista_contatos:
                    print(f"Id: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    print('-' * 30)

        # Consultar por Id
        elif opcao == '2':
            id_consulta = int(input('Digite o Id do contato: '))
            print('-' * 50)
            encontrado = False
            for contato in lista_contatos:
                if contato['id'] == id_consulta:
                    print(f"Id: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    print('-' * 30)
                    encontrado = True
                    break
            if not encontrado:
                print('Contato não encontrado.')

        # Consultar por Atividade
        elif opcao == '3':
            atividade_consulta = input('Digite a Atividade: ')
            print('-' * 50)
            encontrados = 0
            for contato in lista_contatos:
                if contato['atividade'].lower() == atividade_consulta.lower():
                    print(f"Id: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}")
                    print('-' * 30)
                    encontrados += 1
            if encontrados == 0:
                print('Nenhum contato encontrado com essa atividade.')

        #Retornar ao menu
        elif opcao == '4':
            return

        # Opção inválida
        else:
            print('Opção inválida. Tente novamente.')


 #Função para remover contato
def remover_contato():
    """Função que remove um contato da lista pelo Id"""
    while True:
        print('-' * 50)
        print('---------- MENU REMOVER CONTATO ----------')
        id_remover = int(input('Digite o Id do contato a ser removido: '))

        # Procurando e removendo o contato
        encontrado = False
        for i, contato in enumerate(lista_contatos):
            if contato['id'] == id_remover:
                lista_contatos.pop(i)
                print('Contato removido com sucesso!')
                print('-' * 50)
                encontrado = True
                return  # Sai da função após remover

        # Se não encontrou o id
        if not encontrado:
            print('Id inválido. Tente novamente.')


#MENU PRINCIPAL
while True:
    print()
    print('-' * 50)
    print('--------------- MENU PRINCIPAL ---------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Contato')
    print('2 - Consultar Contato(s)')
    print('3 - Remover Contato')
    print('4 - Sair')
    opcao_menu = input('>> ')

  #Cadastrar Contato
    if opcao_menu == '1':
        cadastrar_contato(id_global)
        id_global += 1  # Incrementa o id após cadastrar

    elif opcao_menu == '2':
        consultar_contatos()

    elif opcao_menu == '3':
        remover_contato()

    elif opcao_menu == '4':
        print('Encerrando o programa. Até logo!')
        break  # Encerra o loop e o programa

    else:
        print('Opção inválida. Tente novamente.')
