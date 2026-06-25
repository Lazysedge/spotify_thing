from pathlib import Path


def check_ffmpeg():
    ffmpeg_path = Path(
        "ffmpeg/ffmpeg.exe"
    )

    if ffmpeg_path.exists():
        print(
            "\nFFmpeg found locally."
        )
        print(
            f"Location: {ffmpeg_path}"
        )
        return True

    print(
        "\nFFmpeg not found."
    )

    print(
        "Expected location:"
    )

    print(
        "ffmpeg/ffmpeg.exe"
    )

    return False