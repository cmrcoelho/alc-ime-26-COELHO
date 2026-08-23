import numpy as np


def matrix_product(A, B):
    """Return the product of an m x n matrix and a p x q matrix."""
    A = np.asarray(A)
    B = np.asarray(B)

    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("A and B must both be two-dimensional matrices")

    m, n = A.shape
    p, q = B.shape

    if n != p:
        raise ValueError(f"Matrix product is undefined because n ({n}) != p ({p})")

    return A @ B


if __name__ == "__main__":
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    B = np.array([[7, 8],
                  [9, 10],
                  [11, 12]])

    print(matrix_product(A, B))
