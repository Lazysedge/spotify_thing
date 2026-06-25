import shutil


def ffmpeg_exists():
    return shutil.which("ffmpeg") is not None


def check_ffmpeg():

    if ffmpeg_exists():
        print("FFmpeg detected.")
        return True

    print("FFmpeg not found.")
    return False