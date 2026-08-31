import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    x_arr = np.asarray(x)
    p_arr = np.asarray(p)

    ## This is just dot product of x and p
    #sum = (x_arr * p_arr).sum()
    #return float(sum)

    return float(np.dot(x,p))