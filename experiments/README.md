# Experiments

Keep each experiment reproducible: record its objective, dataset version and terms, preprocessing, split strategy, model settings, random seed, metrics, and known limitations.

## Existing preliminary pilot

The earlier Kaggle notebook used UrbanSound8K to explore a binary `gunfire_like` versus `other_sound` task with MFCC summary features and a scikit-learn classifier. Preserve the original notebook and its outputs when exporting it into this folder. Treat its scores as preliminary event-detection results only; they do not answer the game-versus-real source question.

Before using those results in the thesis, verify the exact split construction, thresholds, metrics, and whether any related recordings crossed between splits.
