import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    n = len(A)
    m = len(A[0])

 
    np_array = np.empty((m,n),dtype = type(A[0]))

    for i in range(n):
        for j in range(m):
            np_array[j,i] = A[i][j]

    return np_array

