import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """

    np_array = np.array(A)
    
    return np_array.T
    
    pass
