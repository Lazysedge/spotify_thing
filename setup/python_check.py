import sys


MIN_MAJOR = 3
MIN_MINOR = 10


def check_python_version():
    major = sys.version_info.major
    minor = sys.version_info.minor

    if (
        major < MIN_MAJOR or
        (major == MIN_MAJOR and minor < MIN_MINOR)
    ):
        raise RuntimeError(
            f"Python {MIN_MAJOR}.{MIN_MINOR}+ required.\n"
            f"Current version: {major}.{minor}"
        )

    print(
        f"[OK] Python version "
        f"{major}.{minor}"
    )