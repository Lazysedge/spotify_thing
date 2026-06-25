from spotify_client import get_spotify_client

from playlist_manager import (
    show_user_info,
    choose_playlist,
    get_all_tracks,
    print_tracks,
    get_playlist_name
)

from duplicate_detector import (
    find_fuzzy_duplicates,
    remove_duplicates
)

from csv_exporter import (
    export_playlist_to_csv
)

from setup.first_run import (
    run_first_run_checks
)

from downloader.spotify_downloader import (
    SpotifyDownloader
)

from downloader.csv_downloader import (
    download_csv_playlist
)

# ----------------------------------------
# First run checks
# ----------------------------------------
run_first_run_checks()

# ----------------------------------------
# Connect to Spotify
# ----------------------------------------
sp = get_spotify_client()

# ----------------------------------------
# Show account information
# ----------------------------------------
show_user_info(sp)

# ----------------------------------------
# Choose playlist
# ----------------------------------------
playlist_id = choose_playlist(sp)

# ----------------------------------------
# Load tracks
# ----------------------------------------
tracks = get_all_tracks(
    sp,
    playlist_id
)

print(
    f"\nLoaded {len(tracks)} tracks."
)

# ----------------------------------------
# Playlist name
# ----------------------------------------
playlist_name = get_playlist_name(
    sp,
    playlist_id
)

safe_filename = (
    playlist_name
    .replace("/", "-")
    .replace("\\", "-")
)

# ----------------------------------------
# Export CSV
# ----------------------------------------
csv_filename = (
    f"{safe_filename}.csv"
)

export_playlist_to_csv(
    tracks,
    csv_filename
)

# ----------------------------------------
# Print tracks
# ----------------------------------------
print_tracks(tracks)

# ----------------------------------------
# Duplicate detection
# ----------------------------------------
duplicates = find_fuzzy_duplicates(
    tracks,
    similarity_threshold=90,
    max_duration_difference=10000
)

print(
    f"\nFound {len(duplicates)} possible duplicates."
)

if len(duplicates) > 0:

    answer = input(
        "\nRemove duplicates? (y/n): "
    ).lower()

    if answer == "y":

        remove_duplicates(
            sp,
            playlist_id,
            duplicates
        )

# ----------------------------------------
# Main menu
# ----------------------------------------
while True:

    print("\n==============================")
    print("Spotify AI Menu")
    print("==============================")
    print("1. Export playlist to CSV")
    print("2. Download playlist")
    print("3. Download using CSV")
    print("4. Detect duplicates")
    print("5. Exit")

    choice = input(
        "\nChoose option: "
    )

    # ------------------------------------
    # Export CSV
    # ------------------------------------
    if choice == "1":

        export_playlist_to_csv(
            tracks,
            csv_filename
        )

    # ------------------------------------
    # Download playlist
    # ------------------------------------
    elif choice == "2":

        downloader = SpotifyDownloader()

        playlist_url = (
            f"https://open.spotify.com/playlist/"
            f"{playlist_id}"
        )

        print(
            "\nStarting playlist download..."
        )

        downloader.download_playlist(
            [playlist_url],
            "downloads",
            "mp3"
        )

    # ------------------------------------
    # Download from CSV
    # ------------------------------------
    elif choice == "3":

        print(
            "\nDownloading using CSV..."
        )

        download_csv_playlist(
            csv_filename,
            "downloads"
        )

    # ------------------------------------
    # Duplicate detection again
    # ------------------------------------
    elif choice == "4":

        duplicates = find_fuzzy_duplicates(
            tracks,
            similarity_threshold=90,
            max_duration_difference=10000
        )

        print(
            f"\nFound "
            f"{len(duplicates)} "
            f"duplicates."
        )

    # ------------------------------------
    # Exit
    # ------------------------------------
    elif choice == "5":

        print(
            "\nGoodbye."
        )

        break

    else:

        print(
            "\nInvalid option."
        )