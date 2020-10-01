#!/usr/bin/python3
# Generate a solution table for Shut The Box
# Bart Massey

import collections

import choices

# Compute the powerset of box states.
def box_states():
    return powerset(list(range(1,10)))

# Compute the powerset of a set.
def powerset(digits):
    # The powerset of the empty set
    # just contains the empty set.
    if digits == []:
        return {frozenset()}

    # Peel an element off the digit list.
    first = digits[0]
    rest = digits[1:]

    # Find the powerset for the rest.
    base = powerset(rest)

    # Add first to each element of base to
    # get unique new sets.
    fbase = {frozenset(s | {first}) for s in base}

    # Return the whole mess.
    return base | fbase

# Compute die roll probabilities.
def roll_probs():
    probs = collections.defaultdict(lambda: 0)
    count = 0
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            count += 1
            probs[d1 + d2] += 1
    for r in probs:
        probs[r] /= count
    return probs

# Unit tests.
if __name__ == '__main__':

    import unittest

    class TestsPowerset(unittest.TestCase):

        # Nothing gives nothing.
        def test_empty_list(self):
            p = powerset([])
            self.assertEqual(p, {frozenset()})

        # One gives two.
        def test_singleton_list(self):
            p = powerset([1])
            self.assertEqual(p, {frozenset(), frozenset({1})})

        # Two gives four.
        def test_singleton_list(self):
            p = powerset([1, 2])
            self.assertEqual(p, {
                frozenset(),
                frozenset({1}),
                frozenset({2}),
                frozenset({1, 2}),
            })

    class TestsDieProb(unittest.TestCase):

        # Probability of 7.
        def test_seven(self):
            ps = roll_probs()
            self.assertTrue(abs(ps[7] - 1/6) < 0.001)

        # Probability of 2.
        def test_two(self):
            ps = roll_probs()
            self.assertTrue(abs(ps[2] - 1/36) < 0.001)

        # Probability of 12.
        def test_two(self):
            ps = roll_probs()
            self.assertTrue(abs(ps[12] - 1/36) < 0.001)

    unittest.main()
