from sklearn.cluster import KMeans


def cluster_songs(
    embeddings,
    n_clusters=5
):
    model = KMeans(
        n_clusters=n_clusters,
        random_state=42
    )

    labels = model.fit_predict(
        embeddings
    )

    return labels