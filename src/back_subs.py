import numpy as np


def back_substitution(U, b):
    """Solve U x = b for x where U is upper-triangular.

    Parameters
    - U: 2-D square numpy array (upper triangular)
    - b: 1-D array-like of length n

    Returns
    - x: 1-D numpy array solution

    Raises ValueError if shapes are incompatible or diagonal contains zeros.
    """
    U = np.asarray(U)
    b = np.asarray(b)

    if U.ndim != 2:
        raise ValueError("U must be a 2-D array")
    n, m = U.shape
    if n != m:
        raise ValueError("U must be square")
    if b.ndim != 1 or b.size != n:
        raise ValueError("b must be a 1-D array of length n")

    # Allow tiny numerical noise below the diagonal.
    if not np.allclose(U, np.triu(U), atol=1e-12, rtol=0.0):
        raise ValueError("U must be upper-triangular")

    x = np.zeros(n, dtype=np.result_type(U, b, float))

    for i in range(n - 1, -1, -1):
        diag = U[i, i]
        if diag == 0:
            raise ValueError(f"Zero diagonal element at index {i}")
        if i == n - 1:
            s = 0.0
        else:
            # Use the solution values already computed.
            s = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - s) / diag

    return x


if __name__ == "__main__":
    # Simple self-test
    rng = np.random.default_rng(0)
    n = 5
    A = rng.standard_normal((n, n))
    U = np.triu(A)
    # make diagonal safely non-zero
    U[np.diag_indices(n)] += np.arange(1, n + 1)

    x_true = rng.standard_normal(n)
    b = U @ x_true

    x = back_substitution(U, b)

    print("x computed:", x)
    print("x true:    ", x_true)
    assert np.allclose(x, x_true)
    print("Back substitution test passed.")
