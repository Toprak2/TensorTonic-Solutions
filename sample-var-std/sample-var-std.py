import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    arr = np.asarray(x,dtype=float)

    mean = np.mean(arr)
    sum = 0.0
    
    
    for num in arr:
        sum += (num - mean)**2

    variance= float(sum)/(len(arr)-1)
    deviation = float(np.sqrt(variance))
    
    return {"variance":variance,"standard_deviation":deviation}
    
    pass