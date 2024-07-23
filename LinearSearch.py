from typing import List

haystack = [1, 23, 54, 3, 898, 445]
needle = 23


# * Implementing a linear search (Python's "if i in list:" is a linear search)
def linear_search(haystack: List, needle: int) -> List:
    for i in range(len(haystack)):
        if haystack[i] == needle:
            print(f'Found it at {i}')
            return True
        
    print('Not found')
    return False


linear_search(haystack, needle)
        