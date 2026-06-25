from ai.similarity_engine import (
    cosine_similarity
)


def compare_songs(
    features_a,
    features_b
):
    score = cosine_similarity(
        features_a["mfcc"],
        features_b["mfcc"]
    )

    return score


def are_duplicates(
    features_a,
    features_b,
    threshold=0.95
):
    score = compare_songs(
        features_a,
        features_b
    )

    return score >= threshold