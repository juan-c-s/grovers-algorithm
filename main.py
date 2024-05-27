import numpy as np
import math 

def hadamardN( n : int):
    base = np.full((2,2), 1/math.sqrt(2))
    base[1][1] *= -1
    hadamardMatrix = np.full((2,2), 1/math.sqrt(2))
    hadamardMatrix[1][1] *= -1
    for i in range(n-1):
        hadamardMatrix = np.kron(hadamardMatrix, base)
   
    return hadamardMatrix

def projectOverMedian(states, N):
    identidad = np.eye(N)
    matriz = np.full((N, N), 0.0)
    matriz[0][0] = 2.0
    matriz -= identidad
    states @= matriz
    # states = np.kron(states, np.eye(2))
    return states


def phaseInversion(states, oracleMatrix):  
    return states @ oracleMatrix

def normalityCheck(states):
    sum = 0
    for x in states[0]:
        sum += x*x
    assert(sum <= 1.001)


def grover(n : int, f : callable):
    N = 2**n
    iterations = 1
    # iterations = math.pi / 4.0 * math.sqrt(N)
    states = np.full((1,N), 0)
    states[0][0] = 1

    hadamardMatrix = hadamardN(n)
    states = states @ hadamardMatrix
    normalityCheck(states)
    print(states)
    oracleMatrix = np.eye(N)
    for i in range(0,N):
        oracleMatrix[i][i] = ((-1) ** f(i))

    # # print(oracleMatrix)
    # print(oracleMatrix)
    # print(states)
    for _ in range(math.ceil(iterations)):
        states = phaseInversion(states, oracleMatrix)# correr función (Negar los que dan 1 en la función)

        # Inversión de la media
        states = states @ hadamardMatrix
        states = projectOverMedian(states, N)
        states = states @ hadamardMatrix

    return states

def f(x : int):
    return 1 if x == 0 else 0

def main():
    states = grover(2, f)
    print(states)
main()

"""

"""

