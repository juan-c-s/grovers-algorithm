# Proyecto: Implementación del Algoritmo de Grover en Python
## Descripción del Proyecto
Este proyecto implementa el Algoritmo de Grover utilizando operaciones matriciales en Python, sin el uso de bibliotecas que implementen funciones cuánticas. El programa recibe el tamaño del problema y la función oráculo como parámetros, y genera el circuito que implementa el Algoritmo de Grover para esa función oráculo.

## Requisitos
Python 3.x
Numpy
Instalación
Clona o descarga el repositorio del proyecto.

Instala las dependencias necesarias ejecutando el siguiente comando:
```{code}
pip install numpy
```

## Estructura del Proyecto
El proyecto se compone de las siguientes funciones:

hadamardN(n: int)\
projectOverMedian(N: int)\
phaseInversion(N: int, f: callable)\
normalityCheck(states: np.array)\
grover(n: int, f: callable)\
f(x: int)\
main()

## Descripción de las Funciones
1. hadamardN(n: int):
Genera una matriz de Hadamard para n qubits. Esta matriz se utiliza para crear la superposición inicial de los estados cuánticos.
```{code}
def hadamardN(n: int):
    base = np.full((2,2), 1/math.sqrt(2))
    base[1][1] *= -1
    hadamardMatrix = np.full((2,2), 1/math.sqrt(2))
    hadamardMatrix[1][1] *= -1
    for _ in range(n-1):
        hadamardMatrix = np.kron(base, hadamardMatrix)
    hadamardMatrix = np.kron(hadamardMatrix, np.eye(2))
    return hadamardMatrix
```
2. projectOverMedian(N: int):
Genera la matriz de inversión sobre la media para N estados. Esta matriz se utiliza en el paso de amplificación de amplitud del Algoritmo de Grover.
```{code}
def projectOverMedian(N):
    identidad = np.eye(N)
    matriz = np.full((N, N), 0.0)
    matriz[0][0] = 2.0
    matriz -= identidad
    matriz = np.kron(matriz, np.eye(2))
    return matriz
```

3. phaseInversion(N: int, f: callable):
Genera la matriz de inversión de fase basada en la función oráculo f. Esta matriz aplica una inversión de fase a los estados marcados por el oráculo.
```{code}
def phaseInversion(N, f: callable):
    oracleMatrix = np.eye(N)
    for i in range(N):
        oracleMatrix[i][i] = ((-1) ** f(i))
    oracleMatrix = np.kron(np.eye(2), oracleMatrix)
    return oracleMatrix
```
4. normalityCheck(states: np.array):
Verifica que la norma de los estados cuánticos sea aproximadamente 1. Esta función es útil para asegurar que las operaciones cuánticas no desnormalicen el estado.

```{code}
def normalityCheck(states):
    sum = 0
    for x in states[0]:
        sum += x*x
    print(sum)
    assert(sum <= 1.1 and sum >= 0.9)

```

5. grover(n: int, f: callable):
Implementa el Algoritmo de Grover. n es el número de qubits, y f es la función oráculo. La función retorna los estados finales después de aplicar el algoritmo.

```{code}
def grover(n: int, f: callable):
    N = 2**(n+1)
    iterations = math.pi / 4.0 * math.sqrt(N)
    states = np.full((1,2**n), 0)
    states[0][0] = 1
    one = np.full((1,2), 0)
    one[0][1] = 1
    states = np.kron(one, states)
    hadamardMatrix = hadamardN(n)
    phaseInversionMatrix = phaseInversion(2**n, f)
    meanInversionMatrix = projectOverMedian(2**n)
    states = states @ hadamardMatrix
    for _ in range(math.ceil(iterations)):
        states = states @ phaseInversionMatrix
        states = states @ hadamardMatrix
        states = states @ meanInversionMatrix
        states = states @ hadamardMatrix
    return states

```

6. f(x: int):
Define la función oráculo que marca los estados buscados. En este ejemplo, el estado buscado es 0.
```{code}
def f(x: int):
    return 1 if x == 0 else 0
```

## Ejecución del Proyecto
Para ejecutar el proyecto, sigue los siguientes pasos:

1. Clona o descarga el repositorio del proyecto.

2. Instala las dependencias necesarias ejecutando el siguiente comando:
```{code}
pip install numpy
```
3. Ejecuta el archivo principal con el siguiente comando:
```{code}
python main.py
```
