from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    result = {"mean": float(np.mean(x)),"median": float(np.median(x))}

    count = Counter(x)

    smallest = float('inf')
    freq = float('-inf')
    
    for key in count:
        val = count[key]
        if val > freq:
            smallest = key
            freq = val
        elif val == freq and key < smallest:
            smallest = key

    result["mode"] = float(smallest)

    return result