import subprocess


def download_with_spotdl(
    spotify_url,
    output_folder,
    audio_format="mp3"
):

    command = [
        "spotdl",
        spotify_url,
        "--output",
        output_folder,
        "--format",
        audio_format
    ]

    subprocess.run(
        command,
        shell=True
    )