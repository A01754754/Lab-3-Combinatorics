#----------------------------------------------------------
# Lab #3: Combinatorics
# Permutations and combinations with repetitions.
#
# Date: 02-Oct-2026
# Authors:
#           A01754754 Alexis Maximiliano Alva Martínez
#           A01754717 Néstor Daniel Huidobro Aguilar
#----------------------------------------------------------
from pprint import pprint

def nicely_sorted[T](s: list[list[T]]) -> list[list[T]]:

    def size_and_content(value: list[T]) -> tuple[int, list[T]]:
        return (len(value), value)

    return sorted(s, key=size_and_content)


# Complexity: O(2 ^ N)
def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    temp: list[list[T]] = power_set(s[:-1])
    return temp + [e + [s[-1]] for e in temp]


def combinations[T](s: list[T], k: int) -> list[list[T]]:
    return [t for t in power_set(s) if len(t) == k]


def insert[T](x: T, s: list[T], i: int) ->list[T]:
    return s[:i] + [x] + s[i:]


def insert_everywhere[T](x: T, s: list[T]) -> list[list[T]]:
    return [insert(x, s, i) for i in range(len(s) + 1)]


def permute[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    empty: list[list[T]] = []
    return sum([insert_everywhere(s[-1], e) for e in permute(s[:-1])], empty)


def permutations[T](s: list[T], k: int) -> list[list[T]]:
    empty: list[list[T]] = []
    return sum([permute(e) for e in combinations(s, k)], empty)

def permutations_with_repetition[T](s: list[T], k: int) -> list[list[T]]:
    if k == 0:
        return [[]]
    return [
        [x] + e 
        for x in s
        for e in permutations_with_repetition(s, k - 1)
    ]

def combinations_with_repetition[T](s: list[T], k: int) -> list[list[T]]:
    if k == 0:
        return [[]]
    return [
        [s[i]] + e
        for i in range(len(s))
        for e in combinations_with_repetition(s[i:], k - 1)
    ]

if __name__ == '__main__':
    pprint(power_set([]))
    pprint(power_set([1]))
    pprint(power_set(['a', 'b']))
    pprint(nicely_sorted(power_set(['a', 'b', 'c'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    pprint(combinations([1, 2, 3 , 4], 1))
    pprint(sorted(combinations([1, 2, 3 , 4], 2)))
    pprint(sorted(combinations([1, 2, 3 , 4], 3)))
    pprint(sorted(combinations([1, 2, 3 , 4], 4)))
    pprint(sorted(combinations([1, 2, 3 , 4], 0)))
    pprint(insert(7, [1, 2, 3], 0))
    pprint(insert(7, [1, 2, 3], 3))
    pprint(insert(7, [1, 2, 3], 2))
    pprint(insert(7, [1, 2, 3], 1))
    pprint(insert_everywhere(7, [1, 2, 3, 4, 5, 6]))
    pprint(sorted(permutations([1, 2, 3], 1)))
    pprint(sorted(permutations([1, 2, 3], 2)))
    pprint(sorted(permutations([1, 2, 3], 3)))