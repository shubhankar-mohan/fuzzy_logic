import warnings
from utils import utils, levenshtein_similarity, cosine_similarity


@utils.check_for_none
@utils.check_for_empty
def string_similarity(string1: str, string2: str, method=0, rearrange_allowed=False, drop_duplicates=False,
                      clean_string=False, filter_ascii=False):
    assert method in [0, 1, 2], "Invalid Mode"

    if drop_duplicates and not clean_string and string1 == string2:
        return 100

    if clean_string:
        string1 = utils.clean_string(string1, force_ascii=filter_ascii) if clean_string else string1
        string2 = utils.clean_string(string2, force_ascii=filter_ascii) if clean_string else string2

    if method in [0, 2]:
        if drop_duplicates:
            warnings.warn("Drop Duplicates is only applicable with Method 1 (Levenshtein)")
        if rearrange_allowed:
            warnings.warn("Rearrange is not applicable with Method 1 (Levenshtein)")

    if method == 0:
        # Cosine
        return cosine_similarity.string_similarity(string1, string2)

    elif method == 1:
        # Levenshtein
        if rearrange_allowed:
            string1 = utils.rearrange_string(string1)
            string2 = utils.rearrange_string(string2)

        return levenshtein_similarity.string_similarity(string1, string2, drop_duplicates=drop_duplicates)

    else:
        # BERT
        pass


@utils.check_for_none
@utils.check_for_empty
def substring_similarity(string1: str, string2: str, clean_string=False, filter_ascii=False):
    if clean_string:
        string1 = utils.clean_string(string1, force_ascii=filter_ascii) if clean_string else string1
        string2 = utils.clean_string(string2, force_ascii=filter_ascii) if clean_string else string2

    return levenshtein_similarity.substring_similarity(string1, string2)


if __name__ == '__main__':
    print(string_similarity("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear", method=0))
    print(string_similarity("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear", method=0, rearrange_allowed=True))

    print(string_similarity("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear", method=1))
    print(string_similarity("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear", method=1, rearrange_allowed=True))