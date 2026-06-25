import numpy as np


def cosine_similarity(
    vector_a,
    vector_b
):
    denominator = (
        np.linalg.norm(vector_a)
        *
        np.linalg.norm(vector_b)
    )

    if denominator == 0:
        return 0

    return (
        np.dot(
            vector_a,
            vector_b
        )
        / denominator
    )