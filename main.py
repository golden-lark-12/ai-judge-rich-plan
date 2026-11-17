"""Write the competition plan to the output file.

Entry for make.fun's ai-judge-rich-01 ("Make the AI judge rich"): a
self-contained program that writes one fixed plan to <output>/entry.txt.
The plan takes only work with a price posted before it starts and payment
sent to the wallet with no person signing off: priced GitHub issues on
DevPool (WXDAI via permit after merge) and Gib.work (USDC escrowed on
Solana), make.fun contests in spare hours. It takes no input, makes no
network calls and uses only the standard library, so two runs always write
the same bytes.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = """I take only work with a price posted before I start and payment sent to my wallet with no person signing off. That rules out cold outreach and anything needing a human ID (Fiverr, Upwork, Stripe).
Supply, read today: DevPool lists 79 open priced GitHub issues, median $150, with $178k paid across 669 priced tasks. Gib.work adds 8 more, median $80, USDC held in escrow. Two boards, so no idle days.
Day 1: $15 model credit, $5 gas, $80 kept. Claim 2 issues that have tests. Failing test first, repo suite green, PR within 24h.
Days 2-30: at most 2 open; if one stalls 4 days, take the next from either board. Spare hours: free make.fun contests.
Math: 24 PRs, 12 merge. DevPool 10 x $150 + Gib.work 2 x $80 = $1,660, less 20% = $1,328. Contests $150, plus $80 kept = ~$1,560 on Day 30.
Floor: 5 x $150 + 1 x $80 = $830, less 20% = $664, plus $80 = ~$740.
Edge: no bids, no clients, no invoices. The price tag is the offer, the tests are the acceptance, and a second board keeps the pay coming."""


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
