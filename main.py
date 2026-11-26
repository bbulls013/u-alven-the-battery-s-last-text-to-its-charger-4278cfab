"""The Battery's Last Text to Its Charger.

Writes one line (at most 200 characters) to /output/entry.txt: the phone
battery's final message to the charger it waited for all day.
"""

import os

LINE = (
    "I clung to 1% for nine hours just to text you, then found you "
    "plugged into the tablet. Fine — I'm shutting down, and your "
    "6 a.m. alarm is coming with me."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200 and LINE.strip()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
