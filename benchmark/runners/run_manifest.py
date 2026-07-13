"""Run manifest helpers for reproducibility metadata."""


def create(run_id, dataset, adapter, case_ids):
    return {
        "run_id": run_id,
        "dataset": dataset,
        "adapter": adapter,
        "case_ids": list(case_ids),
        "status": "preview",
    }


def add_finding(manifest, case_id, metric, score, flags=None):
    manifest.setdefault("findings", []).append({"case_id": case_id, "metric": metric, "score": score, "flags": flags or []})
    return manifest
