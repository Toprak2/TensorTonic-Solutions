import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    norm_a = 0.0
    norm_b = 0.0
    
    dot_product=0.0
    
    for num1, num2 in zip(a,b):
        dot_product += num1 * num2

        norm_a += num1**2
        norm_b += num2**2

    norm_a = np.sqrt(norm_a)
    norm_b = np.sqrt(norm_b)

    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    
    return float(dot_product/(norm_a*norm_b))
    
    pass