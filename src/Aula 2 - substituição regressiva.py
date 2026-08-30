import numpy as np

def substituicao_regressiva(A, b):
    n = len(b) #pega tamanho do vetor b
    solucao = np.zeros(n) #cria um vetor de zeros para armazenar as soluções

    for i in range(n - 1, -1, -1): #para cada linha da matriz A, começando da última linha até a primeira

        if A[i, i] == 0:
            raise ZeroDivisionError(f"Elemento nulo encontrado na diagonal na posição ({i},{i}).")
           
        soma = 0

        # Soma os termos que estão depois da diagonal principal.
        for j in range(i + 1, n):
            soma = soma + A[i, j] * solucao[j]

        solucao[i] = (b[i] - soma) / A[i, i] #calcula o valor da variável correspondente a linha i, subtraindo a soma dos produtos da equação e dividindo pelo elemento diagonal da matriz A

    return solucao


def main():

    A = np.array([
        [1, 1, -1],
        [0, 1,  -5/2],
        [0, 0,  5/2]
    ], dtype=float)

    b = np.array([2, -1, -8], dtype=float)

    x = substituicao_regressiva(A, b)

    print("Solução:")
    print(f"x1 = {x[0]:.1f}")
    print(f"x2 = {x[1]:.1f}")
    print(f"x3 = {x[2]:.1f}")

if __name__ == "__main__":
    main()
