"""Deterministic benchmark runner for local fixtures."""

from schemas.models import BenchmarkRun, Finding


class BenchmarkRunner:
    def __init__(self, evaluator):
        self.evaluator = evaluator

    def run(self, run_id, dataset, adapter, cases, observations):
        result = BenchmarkRun(run_id=run_id, dataset=dataset, adapter=adapter)
        for case in cases:
            observed = observations.get(case.case_id, "")
            score = float(self.evaluator(case.expected, observed))
            result.add(Finding(case.case_id, case.dimension, score, score >= 0.8, self._message(score)))
        return result

    @staticmethod
    def _message(score):
        if score >= 0.8:
            return "case passed preview threshold"
        if score >= 0.5:
            return "case requires review"
        return "case failed preview threshold"
