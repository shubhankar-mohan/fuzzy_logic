import warnings
from utils import utils, levenshtein_similarity, cosine_similarity


@utils.check_for_none
@utils.check_for_empty
def string_similarity(string1: str, string2: str, method=0, rearrange_allowed=False, drop_duplicates=False,
                      clean_string=False, filter_ascii=False):
    """
    Calculates Similarity between two strings.
    Args:
        string1: string 1
        string2: string 2
        method: (Default: 0) [0, 1, 2] 0 is for Cosine Distance, 1 is for Levenshtein Distance
        rearrange_allowed: [True, False] Is rearrange allowed while calculating similarity. If set to true, sequence
                            of words will be ignored while calculating similarity.
        drop_duplicates: [True, False] Weather to drop duplicates from a sentence. If set to true, all duplicates will
                        be removed.
        clean_string: [True, False] If set to true, remove all non alpha-numeric characters including whitespaces
                                    and make all characters to lower case.
        filter_ascii: [True, False] If set to true, all characters other than ASCII will be removed.

    Returns: A float, representing similarity between string1 and string2.

    """
    assert method in [0, 1], "Invalid Mode"

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
    """
        Returns maximum similarity between all possible sub-strings combinations of two strings based on levenshtein
        similarity.
        Args:
            string1: string 1
            string2: string 2
            clean_string: [True, False] If set to true, remove all non alpha-numeric characters including whitespaces
                                        and make all characters to lower case.
            filter_ascii: [True, False] If set to true, all characters other than ASCII will be removed.

        Returns: A float, representing similarity between string1 and string2.

        """
    if clean_string:
        string1 = utils.clean_string(string1, force_ascii=filter_ascii) if clean_string else string1
        string2 = utils.clean_string(string2, force_ascii=filter_ascii) if clean_string else string2

    return levenshtein_similarity.substring_similarity(string1, string2)
