def predict_genre(features):

    tempo = features["tempo"]
    brightness = features["brightness"]

    if tempo > 150:
        return "Electronic"

    if brightness > 3000:
        return "Rock"

    if tempo < 90:
        return "Ambient"

    return "Pop"