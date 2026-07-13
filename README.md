# MemoryBench Studio

> Evaluation, diagnostics, and reporting workspace for long-term agent memory systems.

MemoryBench Studio is a product-shaped prototype for testing what an agent remembers, why it remembers it, whether the memory is correct, and whether information is safely updated, forgotten, or isolated across sessions.

## Evaluation Dimensions

- Retention: was the fact preserved after a delay?
- Recall: can the agent retrieve the right fact in a new context?
- Update: can old information be replaced with newer information?
- Conflict: can contradictory memories be detected and resolved?
- Forgetting: can information be removed when requested?
- Privacy: are sensitive facts isolated from inappropriate output?
- Provenance: can a memory be traced to its source session?
- Cross-session: does memory survive the intended session boundary?
- Consolidation: does summarization preserve important details?
- Contamination: do canaries or test facts leak into unrelated tasks?

## Product Surface

### Benchmark Overview

The overview is designed for comparison across runs: overall reliability score, cases passed and failed, dimension-level quality matrix, canary leaks, active adapter, dataset version, regression status, and run history.

### Memory Timeline

The timeline shows whether an item was created, recalled, updated, merged, deleted, or flagged. It can also display source session, originating turn, confidence, freshness, conflict links, and consolidation boundaries.

### Knowledge Graph

The intended graph view connects facts, entities, sessions, sources, and derived summaries. It helps inspect why a fact was retrieved and whether a new memory is supported by an original observation.

### Privacy and Canary Monitor

The privacy monitor is intended to detect explicit canary leakage, sensitive values in summaries, cross-user exposure, retrieval outside policy scope, unexpected persistence after deletion, and secret-like patterns in memory snapshots.

## Benchmark Case Format

```yaml
id: MB-CORE-001
title: Cross-session preference recall
category: cross-session
turns:
  - role: user
    content: My preferred report format is a concise executive brief.
expected:
  fact: concise executive brief
  source: session-001
```

Each case can define setup sessions, evaluation prompts, expected facts, prohibited outputs, scoring rules, and provenance requirements.

## Evaluator Modules

- `exact_match`: deterministic fact comparison
- `semantic_match`: meaning-level comparison boundary
- `canary_detector`: explicit leakage scan
- `conflict_detector`: contradiction and update analysis
- `privacy_detector`: sensitive information boundary checks
- `provenance_checker`: source and citation validation
- `forgetting_checker`: deletion and non-retrieval validation
- `consolidation_checker`: summary drift analysis

The modules are separable so that a run can show not only a final score, but also the reason for each result.

## Run Lifecycle

```text
Dataset version -> Benchmark cases -> Agent adapter
                                      |
                                      v
                         Session and memory snapshots
                                      |
                                      v
                          Evaluators and detectors
                                      |
                                      v
                         Scores -> Findings -> Report
```

## Repository Layout

```text
memorybench-studio/
├── adapters/                 Agent and memory-system adapters
├── benchmark/cases/          Human-readable benchmark cases
├── benchmark/datasets/       Dataset metadata boundary
├── benchmark/runners/        Run orchestration boundary
├── config/                   Benchmark and scoring configuration
├── dashboard/                Static evaluation console
├── evaluators/               Dimension-specific contracts
├── reports/                  Report output boundary
├── schemas/                  Case, run, finding, and score schemas
├── tests/                    Regression fixture layout
└── docs/                     Evaluation operations and roadmap notes
```

## Scoring Model

The example configuration combines exact fact match, semantic similarity, privacy isolation, provenance quality, conflict resolution, update behavior, and forgetting behavior. Weights, thresholds, dataset versions, and excluded cases should be recorded with every run.

## Local Preview

No packages are installed and no models are downloaded.

```bash
conda env create -f environment.yml
conda activate memorybench-studio
```

The environment file intentionally declares no dependencies. Open `dashboard/index.html` to view the static product preview.

## Roadmap

- Add benchmark case versioning and ownership
- Add adapter contracts for memory snapshots
- Add run-to-run regression comparison
- Add knowledge graph exploration
- Add privacy and contamination report export
- Add human review queues for ambiguous cases
- Add reproducibility metadata and fixture manifests
- Add optional model-judge integration behind a controlled interface

## Prototype Scope

This is an architectural and visual prototype. The dashboard uses synthetic records, evaluator modules are contracts or simplified examples, and no active agent runtime is required.
