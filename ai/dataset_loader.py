import os


def get_audio_files(dataset_path):
    audio_files = []

    for root, _, files in os.walk(dataset_path):
        for file in files:
            if file.lower().endswith(".mp3"):
                audio_files.append(
                    os.path.join(root, file)
                )

    return audio_files


def count_audio_files(dataset_path):
    return len(
        get_audio_files(dataset_path)
    )


def get_random_audio_file(dataset_path):
    files = get_audio_files(dataset_path)

    if not files:
        return None

    import random
    return random.choice(files)