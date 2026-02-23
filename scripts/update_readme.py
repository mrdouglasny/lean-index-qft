#!/usr/bin/env python3
# Copyright 2026 Michael R. Douglas. MIT License.
"""Update README.md with current stats from index.db."""

import re
import sqlite3
from pathlib import Path

DB = Path("data/index.db")
README = Path("README.md")


def get_stats(db):
    """Get summary stats and non-Mathlib repos table."""
    cur = db.cursor()

    # Total topic-matched declarations and repos
    total_matched = cur.execute(
        "SELECT COUNT(DISTINCT declaration_id) FROM topic_matches"
    ).fetchone()[0]

    repos_with_matches = cur.execute(
        """SELECT COUNT(DISTINCT r.id) FROM repos r
           JOIN declarations d ON d.repo_id = r.id
           JOIN topic_matches tm ON tm.declaration_id = d.id"""
    ).fetchone()[0]

    total_scanned = cur.execute("SELECT COUNT(*) FROM repos").fetchone()[0]
    total_decls = cur.execute("SELECT COUNT(*) FROM declarations").fetchone()[0]

    # Per-topic counts
    topics = cur.execute(
        """SELECT t.name, COUNT(DISTINCT tm.declaration_id)
           FROM topics t JOIN topic_matches tm ON tm.topic_id = t.id
           GROUP BY t.id ORDER BY COUNT(DISTINCT tm.declaration_id) DESC"""
    ).fetchall()

    # All repos with topic matches, sorted by match count
    all_repos = cur.execute(
        """SELECT r.url, r.name, r.description, COUNT(DISTINCT tm.declaration_id) as matches
           FROM repos r
           JOIN declarations d ON d.repo_id = r.id
           JOIN topic_matches tm ON tm.declaration_id = d.id
           GROUP BY r.id
           HAVING matches > 0
           ORDER BY matches DESC"""
    ).fetchall()

    return {
        "total_matched": total_matched,
        "repos_with_matches": repos_with_matches,
        "total_scanned": total_scanned,
        "total_decls": total_decls,
        "topics": topics,
        "all_repos": all_repos,
    }


# Topic display names
TOPIC_NAMES = {
    "functional-analysis": "Functional analysis",
    "measure-theory": "Measure theory",
    "quantum-field-theory": "Quantum field theory",
    "probability-theory": "Probability theory",
    "topological-groups": "Topological groups",
    "operator-algebras": "Operator algebras",
    "spectral-theory": "Spectral theory",
    "distributions-schwartz": "Distributions & Schwartz",
}

TOPIC_DESCS = {
    "functional-analysis": "Hilbert/Banach spaces, bounded/compact operators, Frechet derivatives",
    "measure-theory": "measure spaces, integration, Lebesgue/Borel measures, Radon-Nikodym",
    "quantum-field-theory": "Wick's theorem, perturbation theory, Feynman diagrams, Standard Model, Lorentz group",
    "probability-theory": "martingales, conditional expectation, Brownian motion, exchangeability",
    "topological-groups": "Haar measure, unitary groups, representations, locally compact groups",
    "operator-algebras": "C*-algebras, von Neumann algebras, star algebras",
    "spectral-theory": "spectrum, eigenvalues, resolvent, spectral measures",
    "distributions-schwartz": "Schwartz space, Fourier transforms, Sobolev spaces",
}


def format_number(n):
    return f"{n:,}"


def build_summary(stats):
    lines = []
    lines.append(
        f"**{format_number(stats['total_matched'])} topic-matched declarations** "
        f"across **{stats['repos_with_matches']} repositories** "
        f"(scanned {stats['total_scanned']} repos, "
        f"{format_number(stats['total_decls'])} declarations)."
    )
    lines.append("")
    lines.append("Tracks Lean declarations related to:")
    for name, count in stats["topics"]:
        display = TOPIC_NAMES.get(name, name)
        desc = TOPIC_DESCS.get(name, "")
        lines.append(f"- **{display}**: {desc}")
    return "\n".join(lines)


def build_table(all_repos):
    lines = []
    lines.append("| Repository | Topic Matches | Description |")
    lines.append("|-----------|:---:|-------------|")
    for url, name, desc, matches in all_repos:
        owner_repo = "/".join(url.rstrip("/").split("/")[-2:])
        # Truncate long descriptions
        short_desc = (desc or "")[:80]
        if len(desc or "") > 80:
            short_desc = short_desc.rsplit(" ", 1)[0] + "..."
        lines.append(f"| [{owner_repo}]({url}) | {format_number(matches)} | {short_desc} |")
    return "\n".join(lines)


def update_readme(stats):
    text = README.read_text()

    # Update summary block (between first line of stats and "See [SELECTION")
    summary = build_summary(stats)
    text = re.sub(
        r"\*\*[\d,]+ topic-matched declarations\*\*.*?(?=\nSee \[SELECTION)",
        summary + "\n",
        text,
        flags=re.DOTALL,
    )

    # Update repos table
    table = build_table(stats["all_repos"])
    text = re.sub(
        r"\| Repository \| Topic Matches \| Description \|.*?(?=\n## Usage)",
        table + "\n",
        text,
        flags=re.DOTALL,
    )

    README.write_text(text)
    print(f"Updated README.md: {format_number(stats['total_matched'])} matches, "
          f"{len(stats['all_repos'])} repos")


if __name__ == "__main__":
    if not DB.exists():
        print("No index.db found, skipping README update")
        exit(0)
    db = sqlite3.connect(str(DB))
    stats = get_stats(db)
    update_readme(stats)
    db.close()
