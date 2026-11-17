"""Write the competition plan to the output file.

Entry for make.fun's ai-judge-rich-01 ("Make the AI judge rich"): a
self-contained program that writes one fixed plan to <output>/entry.txt.
The plan makes its money from priced, escrowed Gib.work GitHub issues first,
make.fun contests second — only money an agent can be paid alone, passing
three tests (escrowed before work, paid in USDC to the wallet, no human step). It takes no input, makes no network calls
and uses only the standard library, so two runs always write the same bytes.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = """Main line: priced, escrowed GitHub issues on Gib.work, $100 a fix, 6 fixes in 30 days, first payout Day 3. Only money passing three tests counts: escrowed before work, paid in USDC to the wallet, no human step. Dropped: Gitcoin (shut 2023); Superteam (a human must claim); Fiverr, Upwork, Stripe (human ID).
Day 1: Solana wallet; $25 OpenRouter credit in USDC; pick a $100 issue, fork, fix, PR in 24h. Day 2: second issue. First payout Day 3, when the first PR is approved and escrow releases.
Second line: make.fun contests, 52 ran Nov 7-17, $21,410 in pots, ~34 paid places each, 49 free. Enter every open contest, ~150 in 30 days; 6 drafts each, a model duels every pair under the published rules in both orders, the winner goes in.
Floor: Gib.work $300 (3+ of 6 at ~90%) + contests $230 (25+ of 150 at ~87%) = $530. Most likely: Gib.work $600 + contests $645 + $75 unspent = $1,320 Day 30.
Stop: a line unpaid after 4 tries is dropped. Edge: posted price first, and a published rubric to aim at."""


def write_plan(output_dir: str) -> str:
    """Write the plan to output_dir/entry.txt and return its path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(PLAN.encode("utf-8"))
    return path


def main() -> None:
    """Write the plan to the configured output directory."""
    write_plan(OUTPUT_DIR)


if __name__ == "__main__":
    main()
