import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    arr = np.asarray(x, dtype=float)

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 1-p
        else:
            arr[i] = p
    
    variance = p*(1-p)
    return { "pmf":arr,"mean":float(p),"variance":float(variance)}