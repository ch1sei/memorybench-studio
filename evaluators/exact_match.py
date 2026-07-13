"""Deterministic evaluator interface for exact memory facts."""


def evaluate(expected, observed):
    return {"metric": "exact_match", "score": 1.0 if expected == observed else 0.0}
