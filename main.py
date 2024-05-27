import numpy as np
import math 

def hadamardN( n : int):
    base = np.full((2,2), 1/math.sqrt(2))
    base[1][1] *= -1
    hadamardMatrix = np.full((2,2), 1/math.sqrt(2))
    hadamardMatrix[1][1] *= -1
    for _ in range(n-1):
        hadamardMatrix = np.kron(base,hadamardMatrix)
    hadamardMatrix = np.kron(hadamardMatrix,np.eye(2),)
    # print(hadamardMatrix)
    return hadamardMatrix

def projectOverMedian(N):
    identidad = np.eye(N)
    matriz = np.full((N, N), 0.0)
    matriz[0][0] = 2.0
    matriz -= identidad
    matriz = np.kron(matriz, np.eye(2))
    return matriz


def phaseInversion(N, f : callable):  
    oracleMatrix = np.eye(N)
    for i in range(0,N):
        oracleMatrix[i][i] = ((-1) ** f(i))
    oracleMatrix = np.kron(np.eye(2), oracleMatrix)
    for i in range(N, N*2):
        oracleMatrix[i][i] = 1
    return oracleMatrix

def normalityCheck(states):
    sum = 0
    for x in states[0]:
        sum += x*x
    print(sum)
    assert(sum <= 1.1 and sum >= 0.9)


def grover(n : int, f : callable):
    N = 2**(n+1)
    # iterations = 1
    iterations = math.pi / 4.0 * math.sqrt(N)
    states = np.full((1,2**n), 0)
    states[0][0] = 1
    one = np.full((1,2), 0)
    one[0][1] = 1
    states = np.kron(one, states)# Inicializar en | - >
    # print(states)
    hadamardMatrix = hadamardN(n)
    phaseInversionMatrix = phaseInversion(2**n, f)
    meanInversionMatrix = projectOverMedian(2**n)
    # print(phaseInversionMatrix)
    states = states @ hadamardMatrix
    # print(states)

    for _ in range(math.ceil(iterations)):
        states = states@phaseInversionMatrix

        states = states@hadamardMatrix
        states = states@meanInversionMatrix
        states = states@hadamardMatrix

    return states[:,: N//2]

def f(x : int):
    return 1 if x == 0 else 0

def main():
    states = grover(2, f)
    print(states)
main()

"""

"""

