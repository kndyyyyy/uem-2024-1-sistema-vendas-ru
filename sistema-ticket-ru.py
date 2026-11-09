# Arthur Kendy Nishimuta RA:139099
# Bianca Yuka Kokubu RA:139629
#
# Análise
#
# O objetivo do código é auxiliar a automatizar o processo de vendas de tíquetes do RU da UEM
# A venda dependerá do tipo de usuário, que determinará o valor a ser pago
# Haverá a possibilidade de 3 formas de pagamento: dinheiro, cartão ou PIX
# O sistema será executado no terminal e poderá fazer registros de vendas e criação de relatórios de venda
# ao final do dia, mostrando a relação de compra de tíquetes de cada usuário, tipo de pagamento e receita final

# Entrada de dados
#
# Como os valores dos tíquetes variam de acordo com o tipo de relação que o usuário tem com a
# universidade, necessitamos criar um tipo enumerado para ordenar os tipos de usuários (alunos, servidores públicos
# que recebem até 3 salários mínimos, servidores que recebem mais que 3 salários, docentes e comunidade externa)
# As formas de pagamento também serão considerados como um tipo enumerado.
# Tipo de dados: Enum, dataclass, int, str, condicionais, list

# Saida de dados
#
# Informacoes necessarias para o operador ter ciencia do progresso das vendas no dia
# Tipo de dados: dataclass, int, str, condicionais, list

# Usaremos o math para arredontar os valores de porcentagem utilizados na funcoes de graficos

import math

from enum import Enum, auto

class TipoUsuario(Enum):
    # definição de um tipo enumerado para os tipos de usuario que podem ser selecionados dentro das funções
    ALUNO = auto()
    SERV_MENOR3 = auto()
    SERV_MAIOR3 = auto()
    DOCENTE = auto()
    EXTERNO = auto()

class TipoPagamento(Enum):
    # definição de um tipo enumerado para as formas de pagamento possíveis para identificação e facilitar na chamada dentro das funções
    PIX = auto()
    DINHEIRO = auto()
    CARTAO = auto()

from dataclasses import dataclass

@dataclass
class Tiquete:
    # definição de um tipo estruturado para ser utilizado no retorno das funções que serão implementadas
    usuario: TipoUsuario
    qtde_tiquetes: int
    forma_pagamento: TipoPagamento

# definição das funções necessárias para o código--------------------------------------------------------------------------------------------

# definicao das funcoes necessaria para o processo de vendas---------------------------------------------------------------------------------

def registra_tiquete() -> Tiquete:
    # função responsável por registrar o tiquete, sendo necessária a entrada de dados do tipo de usuário, quantidade solicitada pelo usuário
    # e a forma de pagamento desejada.
     
    print('\n')
    print('SELECIONE UM DOS NÚMEROS ABAIXO PARA ESCOLHER O TIPO DE USUÁRIO:')
    print(' 1 = ALUNO')
    print(' 2 = SERVIDOR QUE RECEBE MENOS DE 3 SALARIOS MINIMOS')
    print(' 3 = SERVIDOR QUE RECEBE MAIS DE 3 SALARIOS MINIMOS')
    print(' 4 = DOCENTE')
    print(' 5 = EXTERNO')
    print('\n')

    invalido = True
    while invalido:
        invalido = False
        usuario = input('Digite o número correspondente ao tipo de usuário: ')

        if usuario == "1":
            user = TipoUsuario.ALUNO
        elif usuario == "2":
            user = TipoUsuario.SERV_MENOR3
        elif usuario == "3":
            user = TipoUsuario.SERV_MAIOR3
        elif usuario == "4":
            user = TipoUsuario.DOCENTE
        elif usuario == "5":
            user = TipoUsuario.EXTERNO
        else:
            print('\n')
            print('Por favor, escolha apenas um numero de 1 a 5')
            print('\n')
            invalido = True

    qtde_tiquetes = int(input('Digite a quantidade de tiquetes que o usuário deseja comprar: '))
            
    print('\n')
    print('SELECIONE UM DOS NÚMEROS ABAIXO PARA ESCOLHER A FORMA DE PAGAMENTO:')
    print(' 1 = CARTAO')
    print(' 2 = DINHEIRO')
    print(' 3 = PIX')
    print('\n')

    invalido3 = True
    while invalido3:
        invalido3 = False

        forma_pagamento = input('Digite o número correspondente à forma de pagamento: ')

        if forma_pagamento == "1":
            pag = TipoPagamento.PIX
        elif forma_pagamento == "2":
            pag = TipoPagamento.DINHEIRO
        elif forma_pagamento == "3":
            pag = TipoPagamento.CARTAO
        else:
            print('\n')
            print('Por favor, escolha apenas um numero de 1 a 3')
            print('\n')
            invalido3 = True

    return Tiquete(user, qtde_tiquetes, pag)

def registrar_venda(tiq: Tiquete) -> list:
    # definição de uma função que faz o registro da venda, puxando os o retorno da função anterior para calcular o valor total da compra
    # e retornar uma lista com o tipo de usuário, valor total da compra e o tipo de pagamento realizado.
    '''
    Exemplos:

    >>> tiq = Tiquete(TipoUsuario.ALUNO, 10, TipoPagamento.PIX)
    >>> registrar_venda(tiq)
    ['ALUNO', 50, 'PIX']

    >>> tiq = Tiquete(TipoUsuario.DOCENTE, 20, TipoPagamento.CARTAO)
    >>> registrar_venda(tiq)
    ['DOCENTE', 200, 'CARTAO']

    >>> tiq = Tiquete(TipoUsuario.SERV_MAIOR3, 15, TipoPagamento.DINHEIRO)
    >>> registrar_venda(tiq)
    ['SERV_MAIOR3', 150, 'DINHEIRO']

    >>> tiq = Tiquete(TipoUsuario.EXTERNO, 10, TipoPagamento.PIX)
    >>> registrar_venda(tiq)
    ['EXTERNO', 190, 'PIX']
    '''
    if tiq.usuario == TipoUsuario.ALUNO or tiq.usuario == TipoUsuario.SERV_MENOR3: 
        v_uni = 5
        v_total = v_uni * tiq.qtde_tiquetes
    elif tiq.usuario == TipoUsuario.SERV_MAIOR3 or tiq.usuario == TipoUsuario.DOCENTE:
        v_uni = 10
        v_total = v_uni * tiq.qtde_tiquetes
    elif tiq.usuario == TipoUsuario.EXTERNO:
        v_uni = 19
        v_total = v_uni * tiq.qtde_tiquetes
    return [tiq.usuario.name, v_total, tiq.forma_pagamento.name]

# funções utilizadas na geração do relatório-----------------------------------------------------------------------------------------------------------

def receita_dia(vendas: list[list]) -> int:
    # cálculo do faturamento total do dia
    '''
    Exemplos:

    >>> vendas = [['ALUNO', 50, 'PIX']]
    >>> receita_dia(vendas)
    50

    >>> vendas = [['DOCENTE', 200, 'CARTAO']]
    >>> receita_dia(vendas)
    200

    >>> vendas = [['SERV_MAIOR3', 150, 'DINHEIRO'], ['EXTERNO', 209, 'PIX']]
    >>> receita_dia(vendas)
    359

    >>> vendas = [['SERV_MENOR3', 50, 'DINHEIRO'], ['EXTERNO', 171, 'PIX']]
    >>> receita_dia(vendas)
    221
    '''
    receita = 0
    for t in vendas:
        receita = receita + t[1]
    return receita

# funções utilizadas na geração do grafico no relatorio-----------------------------------------------------------------------------------------------------------

def conta_tiquete_usuario(tiquetes: list[Tiquete], total_tiquetes: int) -> list[int]:
    # calcula a relação de vendas de tiquetes para cada tipo de usuário, devolvendo o valor em porcentagem
    '''
    Exemplos:

    >>> tiquetes = [Tiquete(TipoUsuario.EXTERNO, 2, TipoPagamento.PIX), Tiquete(TipoUsuario.ALUNO, 8, TipoPagamento.CARTAO)]
    >>> total_tiquetes = 10
    >>> conta_tiquete_usuario(tiquetes, total_tiquetes)
    [80, 0, 0, 0, 20]

    >>> tiquetes = [Tiquete(TipoUsuario.SERV_MENOR3, 15, TipoPagamento.DINHEIRO), Tiquete(TipoUsuario.DOCENTE, 5, TipoPagamento.CARTAO)]
    >>> total_tiquetes = 20
    >>> conta_tiquete_usuario(tiquetes, total_tiquetes)
    [0, 75, 0, 25, 0]

    >>> tiquetes = [Tiquete(TipoUsuario.SERV_MAIOR3, 5, TipoPagamento.DINHEIRO), Tiquete(TipoUsuario.ALUNO, 5, TipoPagamento.PIX)]
    >>> total_tiquetes = 10
    >>> conta_tiquete_usuario(tiquetes, total_tiquetes)
    [50, 0, 50, 0, 0]
    '''
    tiquetes_aluno = 0
    tiquetes_servmenor3 = 0
    tiquetes_servmaior3 = 0
    tiquetes_docente = 0
    tiquetes_externo = 0

    for t in tiquetes:
        if t.usuario == TipoUsuario.ALUNO:
            tiquetes_aluno = tiquetes_aluno + t.qtde_tiquetes
        elif t.usuario == TipoUsuario.SERV_MENOR3:
            tiquetes_servmenor3 = tiquetes_servmenor3 + t.qtde_tiquetes
        elif t.usuario == TipoUsuario.SERV_MAIOR3:
            tiquetes_servmaior3 = tiquetes_servmaior3 + t.qtde_tiquetes
        elif t.usuario == TipoUsuario.DOCENTE:
            tiquetes_docente = tiquetes_docente + t.qtde_tiquetes
        elif t.usuario == TipoUsuario.EXTERNO:
            tiquetes_externo = tiquetes_externo + t.qtde_tiquetes

    porcentagem_aluno = (tiquetes_aluno / total_tiquetes) * 100
    porcentagem_servmenor3 = (tiquetes_servmenor3 / total_tiquetes) * 100
    porcentagem_servmaior3 = (tiquetes_servmaior3 / total_tiquetes) * 100
    porcentagem_docente = (tiquetes_docente / total_tiquetes) * 100
    porcentagem_externo = (tiquetes_externo / total_tiquetes) * 100
    porcentagem_usuario = [math.floor(porcentagem_aluno), math.floor(porcentagem_servmenor3), math.floor(porcentagem_servmaior3), math.floor(porcentagem_docente), math.floor(porcentagem_externo)]
    return porcentagem_usuario

def porcetagem_receita_tipo_pagamento(vendas: list[list], receitatotal: receita_dia) -> list[int]:
    # calcula a relação das formas de pagamento, devolvendo o valor em porcentagem
    '''
    Exemplos:

    >>> vendas = [['ALUNO', 50, 'PIX']]
    >>> receitatotal = 50
    >>> porcetagem_receita_tipo_pagamento(vendas, receitatotal)
    [100, 0, 0]

    >>> vendas = [['DOCENTE', 200, 'CARTAO']]
    >>> receitatotal = 200
    >>> porcetagem_receita_tipo_pagamento(vendas, receitatotal)
    [0, 0, 100]

    >>> vendas = [['SERV_MAIOR3', 150, 'DINHEIRO'], ['EXTERNO', 209, 'PIX']]
    >>> receitatotal = 359
    >>> porcetagem_receita_tipo_pagamento(vendas, receitatotal)
    [58, 41, 0]

    >>> vendas = [['SERV_MENOR3', 50, 'DINHEIRO'], ['EXTERNO', 171, 'PIX']]
    >>> receitatotal = 221
    >>> porcetagem_receita_tipo_pagamento(vendas, receitatotal)
    [77, 22, 0]
    '''
    total_pix = 0
    total_dinheiro = 0
    total_cartao = 0

    for v in vendas:
        if v[2] == "PIX":
            total_pix = total_pix + v[1]
        elif v[2] == "DINHEIRO":
            total_dinheiro = total_dinheiro + v[1]
        elif v[2] == "CARTAO":
            total_cartao = total_cartao + v[1]

    porcentagem_pix = (total_pix / receitatotal) * 100
    porcentagem_dinheiro = (total_dinheiro / receitatotal) * 100
    porcentagem_cartao = (total_cartao / receitatotal) * 100

    porcentagem_pagamentos = [math.floor(porcentagem_pix), math.floor(porcentagem_dinheiro), math.floor(porcentagem_cartao)]
    return porcentagem_pagamentos

def grafico_barra(usuarios: list[str], porcentagem: list[int]):
    # funcao que devolvera as informacoes das vendas num grafico de barra horizontal, utilizando as funcoes anteriores de retorno em porcentagem
    # das relacoes de usuarios e forma de pagamento
    '''
    
    '''

    maior_nome = 0
    igual = "="
    maior_barra = 0
    
    for usuario in usuarios:
        if len(usuario) > maior_nome:
            maior_nome = len(usuario)
    
    for porc in porcentagem:
        if porc // 5 > maior_barra:
            maior_barra = porc // 5
    

    for i in range(len(usuarios)):
        
        user_len = maior_nome - len(usuarios[i])
        barra_len = maior_barra - (porcentagem[i] // 5)
        tam_espacamento = user_len * " " + " " * 2
        espac_barra = barra_len * " " + " " * 2
        barra = '[' + igual * (porcentagem[i] // 5) + ']'
        grafico = usuarios[i] + tam_espacamento + barra + espac_barra + str(porcentagem[i]) + "%"

        print(grafico)

# definição das funções que serão utilizadas na main------------------------------------------------------------------------------------------------

def inicio(vendas: list[list], tiquetes: list[Tiquete]):
    # funcao responsavel pelo terminal do nosso sistema

    total_tiquetes = 0
    sair = False
    while not sair:
        print('\n')
        print('Digite 1 para cadastrar tiquete e registrar uma venda')
        print('Digite 2 para imprimir relatorio ate o momento')
        print('Digite 3 para sair')
        print('\n')

        opcao = input('Escolha uma opcao: ')

        if opcao == "1":
            tiq: Tiquete = registra_tiquete()
            venda = registrar_venda(tiq)

            print('O valor total da venda foi de: ' + str(venda[1]) + ' reais')
            print('\n')
            print(' 1 = CONFIRMAR VENDA.')
            print(' 2 = CANCELAR VENDA.')
            print('\n')
            confirma_venda = input('Deseja confirmar sua venda? Digite um dos valores correspondentes: ')

            if confirma_venda == "1":
                total_tiquetes = total_tiquetes + tiq.qtde_tiquetes
                vendas.append(venda)
                tiquetes.append(tiq)
                print('Venda confirmada com sucesso.')

            else:
                print('\n')
                print('Venda não confirmada.')

        elif opcao == "2":
            if vendas == []:
                print('Relatorio vazio (nao foram registrados venda ate o momento)')
            else:

                print('\n')
                print('A receita total do dia (ate o momento) foi de: ' + str(receita_dia(vendas)) + ' reais')
                print('O total de tiquetes do dia (ate o momento) foram: ' + str(total_tiquetes) + ' tiquetes')

                porcentagem_aluno = conta_tiquete_usuario(tiquetes, total_tiquetes)
                porcentagem_pagamentos = porcetagem_receita_tipo_pagamento(vendas, receita_dia(vendas))
                
                print('\n')
                print('Porcentagem de tiquetes vendidos para cada tipo de usuario no RU')
                grafico_barra(["Aluno", "Serv<=3", "Serv>3", "Docente", "Externo"], porcentagem_aluno)
                print('\n')

                print('Porcentagem das formas de pagamento em relacao a receita total do dia')
                grafico_barra(["PIX", "DINHEIRO", "CARTAO"], porcentagem_pagamentos)

        elif opcao == "3":
            sair = True

        else:
            print('Opcao nao reconhecida pelo sistema')

def main():
    # funcao main

    vendas: list[list] = []
    tiquetes: list[Tiquete] = []
    inicio (vendas, tiquetes)

if __name__ == "__main__":
    main()