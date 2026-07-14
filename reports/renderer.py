"""Simple report renderer with stable output for review fixtures."""

import json


def to_json(run):
    return json.dumps(run.to_dict(), indent=2, sort_keys=True)


def to_markdown(run):
    lines = [f"# Benchmark run {run.run_id}", "", f"- Dataset: {run.dataset}", f"- Adapter: {run.adapter}", f"- Score: {run.score():.2f}", "", "## Findings", ""]
    for finding in run.findings:
        status = "PASS" if finding.passed else "REVIEW"
        lines.append(f"- `{status}` `{finding.case_id}` {finding.metric}: {finding.score:.2f} - {finding.message}")
    return "\n".join(lines) + "\n"
