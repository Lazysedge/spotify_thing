from ai.similarity_engine import (
    cosine_similarity
)


def recommend(
    target_features,
    database,
    top_k=10
):
    scores = []

    for song in database:

        similarity = cosine_similarity(
            target_features["mfcc"],
            song["features"]["mfcc"]
        )

        scores.append(
            (
                similarity,
                song
            )
        )

    scores.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return scores[:top_k]