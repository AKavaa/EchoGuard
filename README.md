# EchoGuard

EchoGuard is a research project exploring how artificial intelligence and machine learning can analyse audio from videos. It focuses on identifying gunfire-like sounds and examining whether they resemble game audio or controlled firearm recordings. The intended prototype will show detected audio events, timestamps, and model estimates to support human review.

## Setup

Use Python 3.11–3.13. From the project folder, create and activate a virtual environment, then install the project and development tools:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
pre-commit install
```

## Quality checks

Run the configured checks before pushing changes:

```bash
pre-commit run --all-files
```
