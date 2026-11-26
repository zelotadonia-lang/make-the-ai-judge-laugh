"""One-line joke entry for make.fun's "Make the AI Judge Laugh".

Writes a single deterministic joke about office life to
/output/entry.txt: UTF-8, no trailing newline, 1-200 code points.

The joke's setup is a dead office plant; the punchline stacks two more
beats on it: Facilities closed the ticket as resolved, and the plant has
since been promoted to supervising the interns. Every office worker has
seen a ticket marked "resolved" that solved nothing.
"""

import os

JOKE = "The office plant died in March. Facilities marked it resolved, and now it supervises the interns."

# The gate allows 1-200 characters; keep the entry inside it by construction.
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
