import numpy as np
import matplotlib.pyplot as plt

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

    return x_l1, y_l1, x_u, y_u


def mostrar_grafico(theta1, theta2, x_l1, y_l1, x_u, y_u):

    x0, y0 = 0.0, 0.0 #origem

    figura, grafico = plt.subplots(figsize=(8, 8))

    grafico.quiver(x0, y0, x_l1, y_l1,angles="xy", scale_units="xy", scale=1,color="blue", width=0.012)
    grafico.quiver(x_l1, y_l1, x_u - x_l1, y_u - y_l1,angles="xy", scale_units="xy", scale=1,
                   color="red", width=0.012)

    # Nomes no meio dos vetores.
    grafico.text(x_l1 / 2, y_l1 / 2, "L1", color="blue", fontsize=13)
    grafico.text((x_l1 + x_u) / 2,(y_l1 + y_u) / 2,"L2",color="red",fontsize=13)

    # Angulos nas bases de L1 e L2.
    grafico.annotate(
        f"theta1 = {theta1:g} graus",
        xy=(x0, y0),
        xytext=(8, -20),
        textcoords="offset points",
    )
    grafico.annotate(
        f"theta2 = {theta2:g} graus",
        xy=(x_l1, y_l1),
        xytext=(8, -20),
        textcoords="offset points",
    )

    grafico.scatter(
        [x0, x_l1, x_u], [y0, y_l1, y_u],
        color="black", zorder=3,
    )
    grafico.axhline(0, color="black", linewidth=0.8)
    grafico.axvline(0, color="black", linewidth=0.8)
    grafico.grid(True, linestyle="--", alpha=0.5)
    grafico.set_aspect("equal")
    grafico.set_xlim(min(x0, x_l1, x_u) - 8, max(x0, x_l1, x_u) + 8)
    grafico.set_ylim(min(y0, y_l1, y_u) - 8, max(y0, y_l1, y_u) + 8)
    grafico.set_xlabel("Eixo x (cm)")
    grafico.set_ylabel("Eixo y (cm)")
    grafico.set_title("Vetores L1 e L2 no plano R2")

    plt.show()


def main():

    try:
        theta1 = float(input(
            "Digite o angulo theta1 em graus: "
        ))
        theta2 = float(input(
            "Digite o angulo theta2 em graus: "
        ))

        x_l1, y_l1, x_u, y_u = calcular_posicoes(theta1, theta2)

        print("Posicao do efetuador final:")
        print(f"X_U = {x_u:.1f} cm")
        print(f"Y_U = {y_u:.1f} cm")

        mostrar_grafico(theta1, theta2, x_l1, y_l1, x_u, y_u)

    except ValueError:
        print("Erro: os angulos devem ser valores numericos.")


if __name__ == "__main__":
    main()
