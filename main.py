# Garante que o campo não esteja vazio e tenha pelo menos 3 caracteres
def negarVazio(msg):
    while True:
        nome = input(msg)
        if len(nome) >= 3:
            return nome
        else:
            print("Entrada inválida. Tente novamente.")


# Função força uma o usuario a escolher uma opcao que esta presente na lista
def forcaOpcao(msg, listaOpcao):
    opcoes = ', '.join(listaOpcao)
    escolha = input(f"{msg}\n{opcoes}\n->").lower()
    listaOpcao = [opcao.lower() for opcao in listaOpcao]
    while escolha not in listaOpcao:
        escolha = input(f"{msg}\n{opcoes}\n->").lower()
    return escolha


# Bubble Sort para ordenar a lista de vagas pela compatibilidade (maior para menor)
def bubble_sort(lista):
    quantidade = len(lista)

    for i in range(quantidade):
        trocas = 0
        for j in range(0, quantidade - i - 1):

            # Ordena em ordem decrescente com base no valor da compatibilidade
            if lista[j][1] < lista[j+1][1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                trocas += 1

        if trocas == 0: # Se não houve trocas, a lista já está ordenada

            break

# Calcula as 3 vagas mais compatíveis com o perfil do usuário
def calcularTop(usuario, vagas):
    resultados = []
    # Compara cada característica do usuário com cada vaga
    for vaga, dados in vagas.items():
        acertos = 0

        for i in usuario["caracteristicas"]:
            if i in dados["caracteristicas"]:
                acertos += 1

        # Calcula compatibilidade percentual
        compatibilidade = (acertos / len(dados["caracteristicas"])) * 100

        # Adiciona tupla (vaga, porcentagem) ao resultado
        resultados.append((vaga, compatibilidade))

    # Ordena os resultados em ordem decrescente
    bubble_sort(resultados)

    # Retorna as 3 primeiras vagas
    return resultados[:3]


# Permite o usuário editar seu nome ou suas características
def editar():
    if usuario["nome"] == "":
        print("Nenhum perfil criado ainda!")
        return

    print("\nO que deseja editar?")
    opcao = forcaOpcao("Escolha:", ["nome", "caracteristicas"])

    # Edita o nome
    if opcao == "nome":
        novoNome = negarVazio("Digite o novo nome: ")
        usuario["nome"] = novoNome
        print("Nome atualizado com sucesso!")


    # Edita as características
    elif opcao == "caracteristicas":
        print("Características atuais:", usuario["caracteristicas"])
        usuario["caracteristicas"] = [] # Limpa características antigas

        print("\nDigite suas novas características (4 no total):")
        while len(usuario["caracteristicas"]) < 4:
            caract = forcaOpcao("Escolha uma característica:", caracteristicasTotais)
            if caract not in usuario["caracteristicas"]:
                usuario["caracteristicas"].append(caract)
            else:
                print("Característica repetida, escolha outra.")


#Dados do usuário
usuario ={
    'nome':'',
    'caracteristicas':[]
}

#Dados das vagas disponíveis
vagas ={
    'Desenvolvedor Júnior': {
        'caracteristicas': ['analítico', 'tecnologia', 'individual','lógico'],
        'descricao': 'Trabalha no desenvolvimento e manutenção de sistemas.'
    },
    'Designer UX': {
        'caracteristicas': ['criativo', 'equipe', 'inovador','observador'],
        'descricao': 'Cria interfaces e experiências visuais para produtos digitais.'
    },
    'Analista de Sustentabilidade': {
        'caracteristicas': ['comunicativo', 'sustentável', 'organizado','empático'],
        'descricao': 'Atua em projetos voltados à responsabilidade ambiental.'
    },
    "Gestor de Projetos": {
        "caracteristicas": ["liderança", "organizado", "comunicativo", "planejador"],
        "descricao": "Coordena equipes e recursos para garantir a entrega de projetos dentro do prazo e do orçamento."
    },
    "Produtor de Conteúdo Digital": {
        "caracteristicas": ["criativo", "comunicativo", "inovador", "expressivo"],
        "descricao": "Cria textos, vídeos e publicações para redes sociais, sites e campanhas de marketing."
    },
    "Coach de Carreira Digital": {
        "caracteristicas": ["empático", "comunicativo", "organizado", "social"],
        "descricao": "Orienta profissionais a se adaptarem às novas carreiras do futuro e aprimorarem suas habilidades."
    }
}

# Lista total de características disponíveis
caracteristicasTotais = ["analítico", "tecnologia", "individual", "lógico",
    "criativo", "equipe", "inovador", "observador",
    "comunicativo", "sustentável", "organizado", "empático",
    "liderança", "planejador", "expressivo", "social"]



# --- MENU PRINCIPAL ---
print("Olá seja Bem-Vindo(a) ao MatchJob")
print("Aqui ajudamos pessoas a descobrirem profissões ou oportunidades de trabalho compatíveis com suas habilidades")

# Exibe menu de opções
while True:
    print("\nMENU:")
    print("1 - Iniciar teste de compatibilidade")
    print("2 - Ver vagas")
    print("3 - Ver perfil")
    print("4 - Editar perfil")
    print("5 - Sair")

    try:
        escolha = int(input("Escolha uma opção: "))

        # Iniciar teste de compatibilidade
        if escolha == 1:
            print("Você será encaminhada para a área de verificação de compatibilidade")
            iniciar = forcaOpcao("Voce deseja iniciar o teste de compatibilidade? ",['s','n'])
            if iniciar == 's':
                usuario['caracteristicas'] = []
                if usuario['nome'] == '': # Cria nome se ainda não existir
                    nomeUsuario = negarVazio("Diga o seu nome: ")
                    usuario['nome'] = nomeUsuario

                print("\nEscolha características que mais se adequem a voce (digite uma por vez):\n")
                while len(usuario['caracteristicas']) < 4: # Seleção das características
                    caracteristicasUsuario = forcaOpcao("Escolha uma característica:", caracteristicasTotais)

                    # Impede repetição de características
                    if caracteristicasUsuario in usuario['caracteristicas']:
                        print("Você já escolheu essa característica! Escolha outra.")
                    else:
                        usuario['caracteristicas'].append(caracteristicasUsuario)

                # Cálculo da compatibilidade
                verCompatibilidade = calcularTop(usuario, vagas)

                print("\nAs 3 vagas mais compatíveis com o seu perfil são:\n")
                for vaga, porcentagem in verCompatibilidade    :
                    print(f"{vaga}: {porcentagem}% de compatibilidade com a vaga. ")
                    print(f"Descrição sobre a vaga: {vagas[vaga]['descricao']}\n")



        # Exibe todas as vagas disponíveis
        elif escolha == 2:
            for vaga, dados in vagas.items():
                print(f"\n{vaga}")
                print(f"Descrição: {dados['descricao']}")



        # Exibe o perfil do usuário
        elif escolha == 3:
            if usuario["nome"] == "":
                print("Nenhum perfil criado ainda!")
            elif usuario["caracteristicas"] == []:
                print("Perfil criado, mas o teste ainda não foi realizado!")
            else:
                print("\n==== PERFIL DO USUÁRIO ====")
                print(f"Nome: {usuario['nome']}")
                print(f"Características: {', '.join(usuario['caracteristicas'])}")

                # Mostra top 3 sem descrição
                verCompatibilidade = calcularTop(usuario, vagas)
                print("\nTop 3 vagas compatíveis com seu perfil:")
                for vaga, porcentagem in verCompatibilidade:
                    print(f" - {vaga} ({porcentagem}%)")


        # Edita o perfil
        elif escolha == 4:
            if len(usuario["nome"]) >= 1:
                editar()
            else:
                print("Não é possível editar, nenhum perfil criado")

        # Finalizando o programa
        elif escolha == 5:
            print("Muito obrigado, até breve!!!")
            break

        else:
            print("Escolha inválida")

        # Tratamento de erro para entradas não numéricas
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

