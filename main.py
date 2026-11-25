"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message for a bug fix that made everything worse
to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Standard library only.
"""

import os

LINE = "fix: fixed the 500 error by returning 404 for everything"


def main():
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 100, "entry must be 1-100 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
