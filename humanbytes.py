"""Human-readable byte sizes. Standard library only."""

import re


_UNITS = ["B", "KB", "MB", "GB", "TB", "PB"]
_SIZE_RE = re.compile(
    r"^\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*(B|KB|MB|GB|TB|PB)\s*$",
    re.IGNORECASE,
)


def format_bytes(n):
    n = float(n)
    for u in _UNITS:
        if abs(n) < 1024 or u == _UNITS[-1]:
            return f"{n:.1f}{u}" if u != "B" else f"{int(n)}B"
        n /= 1024


def parse_bytes(value):
    """Parse a byte size such as ``1.5KB`` into an integer byte count."""
    if not isinstance(value, str):
        raise TypeError("byte size must be a string")

    match = _SIZE_RE.fullmatch(value)
    if match is None:
        raise ValueError(f"invalid byte size: {value!r}")

    number, unit = match.groups()
    multiplier = 1024 ** _UNITS.index(unit.upper())
    return int(float(number) * multiplier)
