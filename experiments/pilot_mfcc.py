import json
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
from sklearn.ensemble import RandomForestClassifier


def load_features(manifest, split, per_class):
    rows = []
    labels = []
    paths = []
    audio_root = Path(manifest["path_root"])

    for label in ("PUBG", "controlled_firearm"):
        clips = [
            clip for clip in manifest["clips"] if clip["split"] == split and clip["class"] == label
        ]

        for clip in clips[:per_class]:
            audio_path = audio_root / clip["relative_path"]
            audio, sample_rate = sf.read(audio_path, dtype="float32", always_2d=True)
            mono = audio.mean(axis=1)
            mfcc = librosa.feature.mfcc(y=mono, sr=sample_rate, n_mfcc=13)

            rows.append(np.concatenate([mfcc.mean(axis=1), mfcc.std(axis=1)]))
            labels.append(label)
            paths.append(audio_path)

    return np.stack(rows), labels, paths


def main():
    manifest_path = Path("data/EchoGuard_pilot_split.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    # Load training data used by the model to learn classification patterns
    X_train, y_train, _ = load_features(manifest, "train", per_class=200)
    print(f"Training features: {X_train.shape}")

    # Initialise Random Forest classifier with N decision trees
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    X_val, y_val, val_paths = load_features(manifest, "validation", per_class=25)
    print(f"Validation features: {X_val.shape}")

    # predict the classes of the validation audio samples
    predictions = model.predict(X_val)
    misclassified = []

    # compare predicted labels with the actual labels
    for audio_path, actual, predicted in zip(val_paths, y_val, predictions, strict=True):
        print(f"Actual: {actual} | Predicted: {predicted}")
        if actual != predicted:
            misclassified.append((audio_path, actual, predicted))

    print(f"\nMisclassified files ({len(misclassified)}):")
    for audio_path, actual, predicted in misclassified:
        print(f"  {audio_path.resolve()}")
        print(f"    Actual: {actual} | Predicted: {predicted}")

    # Calculate model's classification accuracy on the validation dataset
    total = len(y_val)
    correct = total - len(misclassified)
    print(f"\nValidation accuracy: {correct}/{total} ({correct / total:.0%})")


if __name__ == "__main__":
    main()
