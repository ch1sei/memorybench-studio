# MemoryBench Studio

Evaluation and diagnostics workspace for long-term agent memory systems.

This is a dependency-free product prototype. It uses synthetic benchmark records and placeholder evaluators so the repository can communicate the intended architecture without installing packages, downloading models, or requiring an active agent runtime.

## Evaluation Dimensions

Retention, recall, update, conflict handling, forgetting, privacy, provenance, cross-session recall, consolidation, and contamination.

## Local Environment

```bash
conda env create -f environment.yml
conda activate memorybench-studio
```

The environment declares no packages. Open `dashboard/index.html` for the static product preview.
