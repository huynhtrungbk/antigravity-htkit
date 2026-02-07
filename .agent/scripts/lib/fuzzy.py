#!/usr/bin/env python3
"""Fuzzy matching utilities for Antigravity-HTKit help system."""


def levenshtein_distance(s1: str, s2: str) -> int:
    """Standard Levenshtein distance algorithm."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)

    prev_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


def fuzzy_match(word: str, target: str, threshold: int = 2) -> bool:
    """Check if word matches target within edit distance threshold."""
    if len(word) < 3:
        return word == target

    if word == target:
        return True

    len_diff = abs(len(word) - len(target))
    if len_diff > 1:
        return False

    max_edits = min(threshold, len(target) // 3)
    if max_edits < 1:
        return word == target

    return levenshtein_distance(word, target) <= max_edits
