## Fuzzy Logic

The library provides functions for fuzzy string matching, fuzzy round-off of floats and a fuzzy function for dividing an integer into an integer distribution according to given percentage. 



## Requirements

- Python 3.5 or higher

- difflib

- numpy

  

## Installation

Using PIP via PyPI

```
pip install fuzzy_logic
```

Using PIP via Github

```
pip install git+git://github.com/shubhankar-mohan/fuzzy_logic.git
```

Manually via GIT

```xx
git clone git://github.com/shubhankar-mohan/fuzzy_logic.git
cd fuzzy_logic
python setup.py install
```



## Examples

#### Fuzzy Numeric Functions 

-  **Fuzzy Round** - Performs a Rounding off an an float to an integer, based on decimal part.

  ```
  Args:
      x: float value which needs to be rounded
      break_point: (Default: 0.5) threshold for deciding if ceil or floor needs to be returned
  
  Returns: ceil(x) if x-int(x) >= break_point else floor(x)
  ```

  ```python
  >>> from fuzzy_logic import fuzzynumeric
  >>> fuzzynumeric.fuzzy_round(1.6)
  >>> 2
  >>> fuzzynumeric.fuzzy_round(1.6, break_point=0.8)
  >>> 1
  ```
  

- **Fuzzy Distribution** - The function divides a given integer into different percentages which are integer.

  ```
  Args:
      x: Integer which needs to be divided
      multiplier: Percentages in which integer needs to be divided
      round_type: (Default: fuzzy) ['floor', 'ceil', 'fuzzy'], Primary Round Type to be used while getting
                  base distribution.
      break_point: (Default: 0.8) It is needed if round_type is fuzzy. See fuzzy_round for details.
      guider_type: (Default: multiplier) ['multiplier', 'deficit_decimal', 'guider'] It defines how the left out
                    value after Primary Round off needs to be distributed. Multiplier used multiplier argument to
                    distribute, giving preference to highest. deficit_decimal uses decimal_part left after floor,
                    giving preference to highest. guider uses a given distribution for the same.
      guider: Needs is guider_type is guider. It is used to give preference to allocate left out
                    value after Primary Round off.
  
  Returns: A list of integer values, which are closest representation of percentage distribution of x according
          to multiplier.
  ```

  ```python
  >>> from fuzzy_logic import fuzzynumeric
  >>> fuzzynumeric.fuzzy_integer_distribution(5, [.2, .3, .5])
  >>> [1, 1, 3]
  
  >>> fuzzynumeric.fuzzy_integer_distribution(5, [.2, .3, .5], round_type='ceil')
  >>> [1, 2, 2]
  >>> fuzzynumeric.fuzzy_integer_distribution(5, [.2, .3, .5], round_type='floor')
  >>> [1, 1, 3]
  >>> fuzzynumeric.fuzzy_integer_distribution(5, [.2, .3, .5], round_type='fuzzy', break_point=0.3)
  >>> [1, 2, 2]
  
  
  >>> fuzzynumeric.fuzzy_integer_distribution(5, [.2, .3, .5], guider_type='deficit_decimal')
  >>> [1, 1, 3]
  >>> fuzzynumeric.fuzzy_integer_distribution(5, [.333, .333, .333], guider_type='deficit_decimal')
  >>> [1, 2, 2]
  >>> fuzzynumeric.fuzzy_integer_distribution(7, [.2, .3, .5], guider_type='deficit_decimal')
  >>> [1, 2, 4]
  >>> fuzzynumeric.fuzzy_integer_distribution(7, [.2, .3, .5])
  >>> [1, 2, 4]
  
  >>> fuzzynumeric.fuzzy_integer_distribution(7, [.2, .3, .5], round_type='floor', guider_type='deficit_decimal')
  >>> [1, 2, 4]
  >>> fuzzynumeric.fuzzy_integer_distribution(8, [.2, .3, .5], round_type='floor', guider_type='deficit_decimal')
  >>> [2, 2, 4]
  >>> fuzzynumeric.fuzzy_integer_distribution(8, [.2, .3, .5], round_type='floor')
  >>> [1, 2, 5]
  >>> fuzzynumeric.fuzzy_integer_distribution(8, [.2, .3, .5], round_type='floor', guider=[1, 5, 2])
  >>> [1, 3, 4]
  ```

  

#### Fuzzy String Functions 

- **String Similarity** - Calculates Similarity between two strings.

  ```
  Args:
      string1: string 1
      string2: string 2
      method: (Default: 0) [0, 1] 0 is for Cosine Distance and 1 is for Levenshtein Distance
              rearrange_allowed: [True, False] Is rearrange allowed while calculating similarity. If set to true, sequence
              of words will be ignored while calculating similarity.
      drop_duplicates: [True, False] Weather to drop duplicates from a sentence. If set to true, all duplicates will
              be removed.
      clean_string: [True, False] If set to true, remove all non alpha-numeric characters including whitespaces
              and make all characters to lower case.
      filter_ascii: [True, False] If set to true, all characters other than ASCII will be removed.
  
  Returns: A float, representing similarity between string1 and string2.
  ```

  ```python
  >>> from fuzzy_logic import fuzzystring
  
  >>> fuzzystring.string_similarity("mouse keyboard are part of computer", "mouse keyboard are part of computer", method=0)
  >>> 100.0
  >>> fuzzystring.string_similarity("mouse keyboard are part of computer", "mouse keyboard are part of computer.", method=0)
  >>> 100.0
  >>> fuzzystring.string_similarity("mouse keyboard are part of computer", "mouse keyboard are part of the computer", method=0)
  >>> 92.58
  
  >>> fuzzystring.string_similarity("mouse keyboard are part of computer", "mouse keyboard are part of computer", method=1)
  >>> 100.0
  >>> fuzzystring.string_similarity("mouse keyboard are part of computer", "mouse keyboard are part of computer.", method=1)
  >>> 98.59
  >>> fuzzystring.string_similarity("mouse keyboard are part of computer", "mouse keyboard are part of the computer", method=1)
  >>> 94.59
  
  
  >>> fuzzystring.string_similarity("mouse keyboard are part of computer", "keyboard mouse are part of computer", method=1)
  >>> 82.86
  >>> fuzzystring.string_similarity("mouse keyboard are part of computer", "keyboard mouse are part of computer", method=1, rearrange_allowed=True)
  >>> 100.0
  
  
  >>> fuzzystring.string_similarity("mouse mouse keyboard are part of computer", "mouse keyboard are part of computer", method=1)
  >>> 92.11
  >>> fuzzystring.string_similarity("mouse mouse keyboard are part of computer", "mouse keyboard are part of computer", method=1, drop_duplicates=True)
  >>> 100.0
  
  
  ```

  

- **Sub String Similarity** - Returns maximum similarity between all possible sub-strings combinations of two strings based on levenshtein
          similarity.

  ```
  Args:
      string1: string 1
      string2: string 2
      clean_string: [True, False] If set to true, remove all non alpha-numeric characters including whitespaces
      			and make all characters to lower case.
      filter_ascii: [True, False] If set to true, all characters other than ASCII will be removed.
  
  Returns: A float, representing similarity between string1 and string2.
  ```


  ```python
  >>> from fuzzy_logic import fuzzystring
  
  >>> fuzzystring.string_similarity("mouse mouse keyboard are part of computer", "mouse keyboard are part of computer")
  >>> 95.26
  >>> fuzzystring.substring_similarity("mouse mouse keyboard are part of computer", "mouse keyboard are part of computer")
  >>> 100.0
  ```

  

​	