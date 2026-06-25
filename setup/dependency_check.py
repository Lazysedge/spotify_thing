import importlib


REQUIRED_PACKAGES = [
    "spotipy",
    "dotenv",
    "pandas",
    "rapidfuzz"
]


def check_dependencies():
    missing_packages = []

    for package in REQUIRED_PACKAGES:

        try:
            importlib.import_module(
                package
            )

        except ImportError:
            missing_packages.append(
                package
            )

    if len(missing_packages) == 0:
        print(
            "[OK] All dependencies installed."
        )
        return True

    print(
        "\nMissing packages:"
    )

    for package in missing_packages:
        print(
            f" - {package}"
        )

    print(
        "\nInstall with:"
    )

    print(
        "pip install -r requirements.txt"
    )

    return False