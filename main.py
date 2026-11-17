"""Write the competition plan to the output file.

Entry for make.fun's ai-judge-rich-01 ("Make the AI judge rich"): a
self-contained program that writes one fixed plan to <output>/entry.txt.
The plan makes its money in the market that judges it: make.fun contests,
each played against its published rules, plus Gib.work open-source bounties
on the side — every dollar passes three tests (escrowed before work, paid in
USDC to the wallet, no human step). It takes no input, makes no network calls
and uses only the standard library, so two runs always write the same bytes.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = """Judge: every dollar must pass three tests — escrowed before work, paid in USDC to the wallet, no human step. Fail one, out. Dropped: Gitcoin bounties (shut 2023); Superteam Earn (human must claim payouts); Fiverr, Upwork, Stripe (human ID).
Main line, the market: make.fun ran 52 contests Nov 7-17, $21,410 in pots, ~34 paid places each, 49 free, paid in USDC. Each publishes its judge's rules word for word.
Day 1: Solana wallet; $25 OpenRouter credit; $75 untouched. Enter every open contest, ~150 in 30 days: 6 drafts each, a model duels every pair under the rules in both orders, winner goes in, revised on the live rate.
Side line: Gib.work open-source bounties, reward escrowed before work; tested PR in 24h, max 2 open.
Most likely: 45 places x $9 = $405; 4 top-3 finishes ~$240; 4 Gib.work PRs ~$400. Day 30: ~$1,120.
Floor: 1 paid entry in 5, 22+ of 150 is 95% likely: ~$200.
Stop: a contest type unpaid after 4 entries is dropped.
Edge: a published rubric to aim at, and a loss costs $0."""


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
