import warnings
from difflib import SequenceMatcher

import utils


def get_levenshtein_distance(string1, string2):
    m = SequenceMatcher(None, string1, string2)
    return round(100 * m.ratio(), 2)


def string_similarity(string1, string2, drop_duplicates=False):
    if drop_duplicates:
        tokens1 = set(string1.split())
        tokens2 = set(string2.split())

        intersection = tokens1.intersection(tokens2)
        diff_12 = tokens1.difference(tokens2)
        diff_21 = tokens2.difference(tokens1)

        sorted_inter = " ".join(sorted(intersection))
        sorted_12 = " ".join(sorted(diff_12))
        sorted_21 = " ".join(sorted(diff_21))

        sorted_inter = sorted_inter.strip()
        combined_12 = (sorted_inter + " " + sorted_12).strip()
        combined_21 = (sorted_inter + " " + sorted_21).strip()

        return max(
            get_levenshtein_distance(sorted_inter, combined_12),
            get_levenshtein_distance(sorted_inter, combined_21),
            get_levenshtein_distance(combined_12, combined_21)
        )

    return get_levenshtein_distance(string1, string2)


def substring_similarity(string1, string2):
    m = SequenceMatcher(None, string1, string2)
    blocks = m.get_matching_blocks()

    scores = []
    print(blocks)
    for block in blocks:
        if block[2] > 0:
            sub_s1 = string1[block[0]: block[0] + block[2]]
            sub_s2 = string2[block[1]: block[1] + block[2]]
            scores.append(get_levenshtein_distance(sub_s1, sub_s2))
    if len(scores) == 0:
        return 0
    return max(scores)


if __name__ == '__main__':
    print(substring_similarity("my name is shubhankar", 'iam'))

