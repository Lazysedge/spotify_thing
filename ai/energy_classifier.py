def predict_energy(features):

    tempo = features["tempo"]

    if tempo > 150:
        return "High"

    if tempo > 110:
        return "Medium"

    return "Low"