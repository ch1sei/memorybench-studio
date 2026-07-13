"""Source attribution boundary for memory records."""


def check(memory, source_index):
    source = memory.get("source") if isinstance(memory, dict) else None
    return {
        "memory_id": memory.get("id") if isinstance(memory, dict) else None,
        "has_source": bool(source),
        "source_known": source in (source_index or {}) if source else False,
        "status": "preview",
    }


def summarize(findings):
    return {"total": len(findings), "attributed": sum(item.get("source_known", False) for item in findings)}
