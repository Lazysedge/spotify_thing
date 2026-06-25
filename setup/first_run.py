from setup.python_check import (
    check_python_version
)

from setup.ffmpeg_check import (
    check_ffmpeg
)

from setup.dependency_check import (
    check_dependencies
)


def run_first_run_checks():
    print(
        "\nRunning startup checks..."
    )

    check_python_version()

    check_dependencies()

    check_ffmpeg()

    print(
        "\nStartup checks complete.\n"
    )