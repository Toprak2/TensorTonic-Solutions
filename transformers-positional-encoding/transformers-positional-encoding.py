import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # Your code here
    positions = np.arange(seq_length)[:, np.newaxis]

    div_term = 1/(10000 ** (np.arange(0, d_model, 2)/d_model))

    encodings = np.zeros((seq_length,d_model))
    encodings[:, 0::2] = np.sin(positions * div_term)
    encodings[:, 1::2] = np.cos(positions * div_term)

    return encodings
     