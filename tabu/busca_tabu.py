# coding=utf-8
"""
Algorítmo - Busca Tabu

"""
from random import randint


def solucao_inicial(tam):
    solucao = [str(randint(0, 1)) for i in range(tam)]
    return ''.join(solucao)


def avaliacao(solucao):
    produtos = [("P1", 0.751, 999.90), ("P2", 0.0000899, 2911.12),
                ("P3", 0.00350, 2499.90), ("P4", 0.496, 199.90),
                ("P5", 0.400, 4346.99), ("P6", 0.290, 3999.90),
                ("P7", 0.0424, 308.66), ("P8", 0.200, 2999.00),
                ("P9", 0.0544, 429.90), ("P10", 0.0319, 299.29),
                ("P11", 0.635, 849.00), ("P12", 0.870, 1199.89),
                ("P13", 0.498, 1999.90), ("P14", 0.527, 3999.00)]
    peso = 0
    valor = 0

    for indice, char in enumerate(solucao):
        if char == '1':
            # print(produtos[indice])
            peso = peso + produtos[indice][1]
            valor = valor + produtos[indice][2]
    return valor, peso


def gerar_vizinhos(solucao):
    vizinhos = []
    for i in range(len(solucao)):
        lista_bits = list(solucao)
        lista_bits[i] = '1' if solucao[i] == '0' else '0'
        vizinho = ''.join(lista_bits)
        vizinhos.append(vizinho)
    return vizinhos


def movimento_tabu(solucao, vizinho):
    for i in range(len(solucao)):
        if solucao[i] != vizinho[i]:
            return i


def obter_melhor_vizinho(vizinhos, lista_tabu, melhor_solucao, solucao):
    valor_melhor_vizinho = 0
    peso_melhor_vizinho = 0
    melhor_vizinho = vizinhos[0]
    valor_melhor_solucao = avaliacao(melhor_solucao)[0]

    for vizinho in vizinhos:
        valor_vizinho, peso_vizinho = avaliacao(vizinho)

        if valor_vizinho > valor_melhor_vizinho and peso_vizinho <= 3:
            if movimento_tabu(solucao, vizinho) in lista_tabu:
                # Critério de aspiração por objetivo
                if valor_vizinho > valor_melhor_solucao:
                    melhor_vizinho = vizinho
                    valor_melhor_vizinho = valor_vizinho
                    peso_melhor_vizinho = peso_vizinho
            else:
                melhor_vizinho = vizinho
                valor_melhor_vizinho = valor_vizinho
                peso_melhor_vizinho = peso_vizinho
    return melhor_vizinho, valor_melhor_vizinho, peso_melhor_vizinho


def busca_tabu(bits=4, bt_max=2, t=2):
    lista_tabu = []
    iteracao, melhor_iteracao = 0, 0
    solucao = solucao_inicial(bits)
    melhor_solucao = solucao[:]

    while (iteracao - melhor_iteracao) <= bt_max:
        print('Iteração: ', iteracao)

        valor_solucao, peso_solucao = avaliacao(solucao)
        print('Solução corrente: ', solucao)
        print('Avaliação da solução corrente: ', valor_solucao)
        print('Peso da solução corrente: ', peso_solucao)

        vizinhos = gerar_vizinhos(solucao)
        print('Vizinhos: ', vizinhos)

        melhor_vizinho, valor_melhor_vizinho, peso_melhor_vizinho = \
            obter_melhor_vizinho(vizinhos, lista_tabu, melhor_solucao, solucao)

        print('Melhor Vizinho: ', melhor_vizinho)
        print('Avaliação do melhor vizinho: ', valor_melhor_vizinho)
        print('Peso do melhor vizinho: ', peso_melhor_vizinho)

        pos_tabu = movimento_tabu(solucao, melhor_vizinho)
        print('Movimento Tabu: ', pos_tabu)

        solucao = melhor_vizinho[:]

        if len(lista_tabu) < t:
            lista_tabu.append(pos_tabu)
        else:
            lista_tabu.pop(0)
            lista_tabu.append(pos_tabu)
        print('Lista Tabu: ', lista_tabu)

        valor_melhor_solucao, peso_melhor_solucao = avaliacao(melhor_solucao)
        if valor_melhor_vizinho > valor_melhor_solucao and peso_melhor_vizinho <= 3:
            melhor_solucao = melhor_vizinho[:]
            melhor_iteracao += 1

        valor_melhor_solucao, peso_melhor_solucao = avaliacao(melhor_solucao)
        print('Melhor solução: ', melhor_solucao)
        print('Valor da melhor solução: ', valor_melhor_solucao)
        print('Peso da melhor solução: ', peso_melhor_solucao)
        print('Melhor iteração: ', melhor_iteracao)
        print('')

        iteracao += 1

    return melhor_solucao


if __name__ == '__main__':
    busca_tabu(14, 10, 3)

