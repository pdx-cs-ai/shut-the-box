#!/usr/bin/python3
# Generate choices for Shut The Box
# Bart Massey

# All the ways of making the target score as the sum of a
# subset of the given digits. Returns a list of sets.
def choices(digits, target):
    # Target must be nonnegative.
    assert target >= 0
    # Base case: Easy to make nothing.
    if target == 0:
        return [set()]
    # Base case: Can't make a positive target from nothing.
    if not digits:
        return []

    # Work from smallest digit up.
    m = min(digits)
    # Base case: If smallest digit is already greater than
    # target, can't proceed.
    if m > target:
        return []

    # Recursive case: Use the smallest digit or don't.
    result = []
    ndigits = digits - {m}
    # Try using the smallest digit. 
    mchoices =  choices(ndigits, target - m)
    # Solutions will be part of the result, but be sure to
    # include the digit.
    for c in mchoices:
        result += [c | {m}]
    # Try not using the smallest digit.
    result += choices(ndigits, target)
    return result

# Put choices in canonical form by making each
# choice a sorted list and sorting the result.
# Allow either ordering.
def canon_choices(choices, reverse=False):
    return sorted(
        [sorted(list(c), reverse=reverse) for c in choices],
        reverse=reverse
    )

# Unit tests.
if __name__ == '__main__':

    import unittest

    class TestsChoices(unittest.TestCase):

        # Lots of ways to not make a choice.
        def test_empty_choice(self):
            c = canon_choices(choices({1, 4, 6, 7}, 9))
            self.assertEqual(c, [])

        # One way to make a choice.
        def test_single_choice(self):
            c = canon_choices(choices({1, 2, 3}, 6))
            self.assertEqual(c, [[1, 2, 3]])

        # Lots of ways to make a choice.
        def test_complex_choice(self):
            c = canon_choices(choices(set(range(1, 10)), 9))
            self.assertEqual(
                c,
                [[1, 2, 6],
                 [1, 3, 5],
                 [1, 8],
                 [2, 3, 4],
                 [2, 7],
                 [3, 6],
                 [4, 5],
                 [9]]
            )

    unittest.main()
