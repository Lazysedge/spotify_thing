def predict_mood(features):

    tempo = features["tempo"]
    brightness = features["brightness"]

    if tempo > 140:
        return "Energetic"

    if tempo < 80:
        return "Calm"

    if brightness > 2500:
        return "Happy"

    return "Neutral"