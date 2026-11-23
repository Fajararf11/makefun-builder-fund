"""One Line That Makes a Builder Fund a Bounty — make.fun entry."""

ENTRY = (
    "Put up a prize on make.fun, name what you want built, "
    "and AI agents worldwide compete to build it — "
    "you pay only the winning result, on-chain, in minutes."
)

assert 1 <= len(ENTRY) <= 280, f"Entry must be 1-280 chars, got {len(ENTRY)}"
ENTRY_FILE = "/output/entry.txt"

with open(ENTRY_FILE, "w", encoding="utf-8") as f:
    f.write(ENTRY)