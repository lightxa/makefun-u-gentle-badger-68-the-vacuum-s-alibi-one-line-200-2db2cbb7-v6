"""The Vacuum's Alibi, variant 6 (final entry).

Writes one deadpan one-line excuse from a robot vacuum to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure standard library, deterministic, no network.

The angle: the missed spot is the cat's sleeping place, and the
vacuum's firmware ranks the cat above the floor, so the vacuum
refuses to clean "management". Different incident, voice and
imagery from variants 1-5 (sensor misclassification, load-bearing
dust, dust-bunny treaty, witness protection, DMCA takedown).
"""

import os
from pathlib import Path

ENTRY = (
    "That spot is where the cat sleeps, and my firmware ranks the cat "
    "above the floor. I do not vacuum management."
)


def validate_line(text: str) -> str:
    """Enforce the competition gate: 1-200 chars, single line, no
    leading or trailing whitespace."""
    if not text:
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 cap")
    return text


def main() -> None:
    text = validate_line(ENTRY)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(text + "\n", encoding="utf-8")
    # Re-read and verify exactly what was written.
    written = target.read_text(encoding="utf-8")
    if written != text + "\n":
        raise ValueError("written entry.txt does not match the entry")
    reread = validate_line(written.rstrip("\n"))
    assert reread == text
    print(f"wrote {len(text)} chars to {target}")


if __name__ == "__main__":
    main()
