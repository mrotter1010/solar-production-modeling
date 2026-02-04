from __future__ import annotations

from datetime import datetime

_ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-")
_DEFAULT_SEGMENT = "unknown"


def current_run_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H-%M-%S")


def sanitize_segment(value: str | None, default: str = _DEFAULT_SEGMENT) -> str:
    if value is None:
        value = ""
    stripped = value.strip()
    if not stripped:
        return default
    sanitized = "".join(ch if ch in _ALLOWED_CHARS else "_" for ch in stripped)
    return sanitized or default
