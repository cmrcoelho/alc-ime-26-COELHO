import numpy as np

def substituicao_regressiva(A, b):
    n = len(b) #pega tamanho do vetor b
    x = np.zeros(n) #criando um vetor de zeros para armazenar as soluções

    for i in range(n - 1, -1, -1): #para cada linha da matriz A, começando da última linha até a primeira
        soma = A[i, i + 1:] @ x[i + 1:] #calcula a soma dos produtos dos elementos da linha i de A com os elementos correspondentes de x
        x[i] = (b[i] - soma) / A[i, i] #calcula o valor da variável correspondente a linha i, subtraindo a soma dos produtos da equação e dividindo pelo elemento diagonal da matriz A

    return x


def main():

    A = np.array([
        [1, 1, -1],
        [0, 1,  -5/2],
        [0, 0,  5/2]
    ], dtype=float)

    b = np.array([2, -1, -8], dtype=float)

    x = substituicao_regressiva(A, b)

    print("Solução:")
    print(f"x = {x[0]:.1f}")
    print(f"y = {x[1]:.1f}")
    print(f"z = {x[2]:.1f}")

if __name__ == "__main__":
    main()
