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
    X_train, y_train, _ = load_features(manifest, "train", per_class=100)
    print(f"Training features: {X_train.shape}")

    # Initialise Random Forest classifier with N decision trees
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    X_test, y_test, test_paths = load_features(manifest, "test", per_class=25)
    print(f"Test features: {X_test.shape}")

    # predict the classes of the test audio samples
    predictions = model.predict(X_test)
    misclassified = []

    # compare predicted labels with the actual labels
    for audio_path, actual, predicted in zip(test_paths, y_test, predictions, strict=True):
        if actual != predicted:
            misclassified.append((audio_path, actual, predicted))

    print(f"\nMisclassified files ({len(misclassified)}):")
    for audio_path, actual, predicted in misclassified:
        print(f"  {audio_path.resolve()}")
        print(f"    Actual: {actual} | Predicted: {predicted}")

    print("\nCorrect by class:")
    for label in ("PUBG", "controlled_firearm"):
        class_total = y_test.count(label)
        class_errors = sum(actual == label for _, actual, _ in misclassified)
        print(f"  {label}: {class_total - class_errors}/{class_total}")

    # Calculate model's classification accuracy on the test dataset
    total = len(y_test)
    correct = total - len(misclassified)
    print(f"\nTest accuracy: {correct}/{total} ({correct / total:.0%})")


if __name__ == "__main__":
    main()
