# EchoGuard

EchoGuard is a bachelor’s project exploring audio-based detection of gunfire-like events in short videos and whether detected sounds resemble game audio or controlled firearm recordings. The prototype is intended to support human review with event timestamps and model scores. It will not infer intent or make an automatic safety decision.

## Current stage

The UrbanSound8K experiment is a preliminary pilot for detecting gunfire-like audio. It does not establish that game gunfire can be distinguished from real firearm recordings. The next research step is to audit candidate datasets, labels, recording sources, and usage terms before defining the comparison experiment.

## Repository layout

- `src/echoguard/` — reusable application and audio-processing code.
- `experiments/` — experiment notes and notebooks; keep notebooks reproducible.
- `docs/` — dataset audit and research notes.
- `data/` — local dataset location; audio and video files are excluded from Git.

## Setup

Use Python 3.11–3.13. Create and activate a virtual environment, then install the project and development tools:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
pre-commit install
```

FFmpeg must also be installed and available on `PATH` before video audio extraction is implemented. PyTorch is an optional dependency for the later neural-model experiment; the first baseline will use scikit-learn.

## Dataset handling

Do not commit datasets, audio/video clips, model weights, credentials, or private uploads. Before using a dataset, record its source, labels, recording/session identifiers, licence or terms, and permitted use in `docs/dataset-audit.md`. See `data/README.md` for local storage guidance.

## Quality checks

Run the configured checks before pushing changes:

```bash
pre-commit run --all-files
```

The GitHub Actions workflow runs the same checks on pushes and pull requests.
