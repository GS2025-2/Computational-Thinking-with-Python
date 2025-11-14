# Garante que o campo não esteja vazio e tenha pelo menos 3 caracteres
def negarVazio(msg):
    while True:
        nome = input(msg)
        if len(nome) >= 3:
            return nome
        else:
            print("Entrada inválida. Tente novamente.")


# Função força uma o usuario a escolher uma funçao que esta presente na lista
def forcaOpcao(msg, listaOpcao):
    opcoes = ', '.join(listaOpcao)
    escolha = input(f"{msg}\n{opcoes}\n->").lower()
    listaOpcao = [opcao.lower() for opcao in listaOpcao]
    while escolha not in listaOpcao:
        escolha = input(f"{msg}\n{opcoes}\n->").lower()
    return escolha



def bubble_sort(lista):
    quantidade = len(lista)

    for i in range(quantidade):
        trocas = 0
        for j in range(0, quantidade - i - 1):


            if lista[j][1] < lista[j+1][1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                trocas += 1

        if trocas == 0:
            break


# Função que verifica se o usuario escolheu um numero
def verificaNumero(msg):
    num = input(msg)
    while not num.isnumeric():
        print("Erro!")
        num = input(msg)
    return int(num)


def calcularTop(usuario, vagas):
    resultados = []

    # Para cada vaga, calcular compatibilidade
    for vaga, dados in vagas.items():
        acertos = 0

        for i in usuario["caracteristicas"]:
            if i in dados["caracteristicas"]:
                acertos += 1

        compatibilidade = (acertos / len(dados["caracteristicas"])) * 100
        resultados.append((vaga, compatibilidade))

    # Ordena em ordem decrescente pelo segundo elemento (percentual)
    bubble_sort(resultados)

    # Retorna as 3 primeiras vagas
    return resultados[:3]



usuario ={
    'nome':[],
    'caracteristicas':[]
}
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
caracteristicasTotais = ["analítico", "tecnologia", "individual", "lógico",
    "criativo", "equipe", "inovador", "observador",
    "comunicativo", "sustentável", "organizado", "empático",
    "liderança", "planejador", "expressivo", "social"]



print('Seja Bem-vindo')

nomeUsuario = negarVazio("Diga o seu nome: ")
usuario['nome'].append(nomeUsuario)

print("\nEscolha características que mais se adequem a voce (digite uma por vez):\n")
while len(usuario['caracteristicas']) < 4:
    caracteristicasUsuario = forcaOpcao("Escolha uma característica:", caracteristicasTotais)

    if caracteristicasUsuario in usuario['caracteristicas']:
        print("Você já escolheu essa característica! Escolha outra.")
    else:
        usuario['caracteristicas'].append(caracteristicasUsuario)



top3 = calcularTop(usuario, vagas)

print("\nAs 3 vagas mais compatíveis com o seu perfil são:\n")
for vaga, porcentagem in top3:
    print(f"{vaga}: {porcentagem}% de compatibilidade com a vaga. ")
    print(f"Descrição sobre a vaga: {vagas[vaga]['descricao']}\n")


