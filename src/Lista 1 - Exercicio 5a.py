import numpy as np

L1 = 20.0
L2 = 15.0


def calcular_posicoes(theta1, theta2):
    # Converte os angulos de graus para radianos.
    theta1 = np.radians(theta1)
    theta2 = np.radians(theta2)

    # Calcula a posicao da extremidade de L1.
    x_l1 = L1 * np.cos(theta1)
    y_l1 = L1 * np.sin(theta1)

    # Calcula a posicao de L2 em relacao
    # a extremidade de L1.
    x_l2 = L2 * np.cos(theta1 + theta2)
    y_l2 = L2 * np.sin(theta1 + theta2)

    # Calcula a posicao final do efetuador.
    x_u = x_l1 + x_l2
    y_u = y_l1 + y_l2

    return x_u, y_u

def main():

    try:
        theta1 = float(input(
            "Digite o angulo theta1 em graus: "
        ))
        theta2 = float(input(
            "Digite o angulo theta2 em graus: "
        ))

        x_u, y_u = calcular_posicoes(theta1, theta2)

        print("Posicao do efetuador final:")
        print(f"X_U = {x_u:.1f} cm")
        print(f"Y_U = {y_u:.1f} cm")


    except ValueError:
        print("Erro: os angulos devem ser valores numericos.")


if __name__ == "__main__":
    main()
