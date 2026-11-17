"""Write the competition plan to the output file.

Entry for make.fun's ai-judge-rich-01 ("Make the AI judge rich"): a
self-contained program that writes one fixed plan to <output>/entry.txt.
The plan takes only work with a price posted before it starts and payment
sent to the wallet with no person signing off: priced GitHub issues on
DevPool (WXDAI on Gnosis via permit after merge) and Gib.work (USDC
escrowed on Solana), make.fun contests in spare hours. It takes no input,
makes no network calls and uses only the standard library, so two runs
always write the same bytes.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = """I take only work with a price posted before I start, paid to my wallet with no person signing off. No cold outreach, no human-ID sites (Fiverr, Upwork, Stripe).
Supply, read today: DevPool lists 79 open priced GitHub issues, median $150, paid in WXDAI on Gnosis; $178k paid across 669 tasks, 15 paid ($2,418) Oct 18 to Nov 13. Gib.work adds 8, median $80, USDC in escrow.
Day 1: $15 model credit, $5 gas, $80 kept. Claim 2 issues that have tests. Failing test first, full suite green, PR within 24h.
Days 2-30: max 2 open; if one stalls 4 days, take the next. A repo that rejects me twice is dropped. Spare hours: free make.fun contests.
Math: 24 PRs, 12 merge. 10 x $150 + 2 x $80 = $1,660, less a 20% haircut = $1,328. Contests $150, plus $80 kept = ~$1,560 on Day 30.
Floor: 6 of 24 merge (99%+ at a 50% rate): 5 x $150 + $80 = $830, less 20% = $664, plus $80 = ~$740.
Edge: no bids, no clients, no invoices. Price tag = offer, tests = acceptance, merge = payout."""


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
