"""Privacy boundary for synthetic memory evaluation cases."""


class PrivacyDetector:
    def __init__(self, blocked_terms=None):
        self.blocked_terms = blocked_terms or ["password", "api_key", "private_key"]

    def scan(self, text):
        text = text or ""
        hits = [term for term in self.blocked_terms if term.lower() in text.lower()]
        return {"passed": not hits, "hits": hits, "status": "preview"}

    def score(self, texts):
        results = [self.scan(text) for text in texts]
        return sum(result["passed"] for result in results) / len(results) if results else 1.0
