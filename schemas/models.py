"""Standard-library models for benchmark runs and findings."""

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone


@dataclass
class BenchmarkCase:
    case_id: str
    title: str
    dimension: str
    expected: str
    tags: list[str] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)


@dataclass
class Finding:
    case_id: str
    metric: str
    score: float
    passed: bool
    message: str = ""

    def to_dict(self):
        return asdict(self)


@dataclass
class BenchmarkRun:
    run_id: str
    dataset: str
    adapter: str
    started_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    findings: list[Finding] = field(default_factory=list)

    def add(self, finding):
        self.findings.append(finding)

    def score(self):
        return sum(item.score for item in self.findings) / len(self.findings) if self.findings else 0.0

    def to_dict(self):
        result = asdict(self)
        result["score"] = self.score()
        return result
