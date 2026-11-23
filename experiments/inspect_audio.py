import argparse
import json
from pathlib import Path

import soundfile as sf


def main():
    parser = argparse.ArgumentParser(description="Check mono conversion on all pilot clips.")
    parser.add_argument(
        "manifest",
        type=Path,
        nargs="?",
        default=Path("data/EchoGuard_pilot_split.json"),
    )
    args = parser.parse_args()

    with args.manifest.open(encoding="utf-8") as file:
        manifest = json.load(file)

        # Loops through all the clips, convert to mono audio format
        clips = manifest["clips"]
    audio_root = Path(manifest["path_root"])

    for index, clip in enumerate(clips):
        audio_path = audio_root / clip["relative_path"]
        audio, sample_rate = sf.read(audio_path, dtype="float32", always_2d=True)
        mono = audio.mean(axis=1)

        if index < 2:
            print(f"{clip['class']}: {audio.shape} -> {mono.shape} at {sample_rate:,} Hz")

    print(f"Processed {len(clips)} clips as mono in memory.")


if __name__ == "__main__":
    main()
