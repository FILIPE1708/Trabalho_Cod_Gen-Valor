import random

from ag import AlgoritmoGenetico

dados = ['x', 'y', 'z']


def novoIndividuo(dados):

    genes = []

    for i in range(len(dados)):
        num = random.randint(0, 75)
        genes.append(num)

    return genes


def novaMutacao(genes):

    numAleatorio = random.randint(0, len(genes) - 1)
    num = random.randint(0, 75)
    genes[numAleatorio] = num

    return genes


def funcaoFitness(genes, dados):

    equacao = 5 * genes[0] + 3 * genes[1] - genes[2]
    result = equacao - 39

    if (result < 0):
        return abs(result)

    return result


ag = AlgoritmoGenetico(dados, funcaoFitness=funcaoFitness, maiorFitness=False, tamPopulacao=200)
ag.funCriaIndividuo = novoIndividuo
ag.mutacao = novaMutacao
ag.executa()

print(ag.populacao)
print(ag.melhorResultado())

