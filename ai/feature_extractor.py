import librosa
import numpy as np


def extract_features(audio_path):
    try:
        y, sr = librosa.load(
            audio_path,
            duration=30
        )

        tempo, _ = librosa.beat.beat_track(
            y=y,
            sr=sr
        )

        mfcc = librosa.feature.mfcc(
            y=y,
            sr=sr,
            n_mfcc=13
        )

        chroma = librosa.feature.chroma_stft(
            y=y,
            sr=sr
        )

        spectral_centroid = (
            librosa.feature.spectral_centroid(
                y=y,
                sr=sr
            )
        )

        return {
            "tempo": float(tempo),
            "mfcc": np.mean(
                mfcc,
                axis=1
            ),
            "chroma": np.mean(
                chroma,
                axis=1
            ),
            "brightness": float(
                np.mean(
                    spectral_centroid
                )
            )
        }

    except Exception as e:
        print(
            f"Feature extraction failed: {e}"
        )
        return None