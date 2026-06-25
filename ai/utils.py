import os


def ensure_directory(path):

    if not os.path.exists(path):
        os.makedirs(path)


def seconds_to_minutes(seconds):

    minutes = seconds // 60
    seconds = seconds % 60

    return (
        f"{minutes}:{seconds:02}"
    )