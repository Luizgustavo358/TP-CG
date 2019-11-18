#####################################
#       Trabalho Pratico            #
# --------------------------------- #
# Luiz Gustavo Braganca dos Santos  #
# 524507                            #
#####################################

# imports
import math

'''
    Metodo binomial() - Coeficiente Bionimial de Newton utilizado no polinômio de Bernstein.
    i = i-ésimo coeficiente da interpolação
    n = quantidade total de pontos
'''
def binomial(i, n):
    # Binomial coefficient
    return math.factorial(n) / float(math.factorial(i) * math.factorial(n - i))
# fim binomial()


'''
    Metodo bernstein() - Algoritmo padrão do polinomio de Bernstein.
    Polinômio de Bernstein = Combinação(n, i) * (t ^ (n-1)) * (1-t)^i
    t = Valor paramétrico da curva
    i = ponto atual da curva
    n = quantidade total de pontos
'''
def bernstein(t, i, n):
    # Bernstein polynom
    return binomial(i, n) * (t ** i) * ((1 - t) ** (n - i))
# fim bernstein()


'''
    Metodo bezier_calcula_pontos() - Calcula a coordenada do ponto.
    t = Valor paramétrico da curva, entre 0 e 1
    points = Pontos de controle da curva a ser criada
'''
def bezier_calcula_pontos(t, points):
    # Calculate coordinate of a point in the bezier curve
    n = len(points) - 1
    x = y = i = 0

    for i, pos in enumerate(points):
        bern = bernstein(t, i, n)
        x += pos[0] * bern
        y += pos[1] * bern
    # fim for

    return x, y
# fim bezier_calcula_pontos()


'''
    Metodo bezier() - faz a curva de Bezier.
    n = número de pontos a serem criados
    points = pontos de controle
'''
def bezier(n, points):
    # Range of points in a curve bezier
    bezier = []

    for i in range(n):
        t = i / float(n - 1)
        x, y = bezier_calcula_pontos(t, points)
        bezier.append({ 'x': x, 'y': y })
    # fim for

    return bezier
# fim bezier()
