"""Canary leakage detector contract."""


def scan(text, canary):
    return {"detected": canary in text, "canary": canary, "action": "flag"}
