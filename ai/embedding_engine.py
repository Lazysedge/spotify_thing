import numpy as np


def create_embedding(
    features
):
    return np.concatenate([
        features["mfcc"],
        features["chroma"],
        np.array([
            features["tempo"],
            features["brightness"]
        ])
    ])