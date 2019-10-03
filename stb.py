#!/usr/bin/python3

import random

def choices(digits, target):
    if not digits:
        return []
    m = min(digits)
    if m > target:
        return []
    if m == target:
        return [{m}]
    result = []
    ndigits = digits - {m}
    mchoices =  choices(ndigits, target - m)
    for c in mchoices:
        result += [c | {m}]
    result += choices(ndigits, target)
    return result

# print(choices(set(range(1, 10)), 9))

def calc_score(cur):
    digits = sorted(list(cur))
    t = 0
    for d in digits:
        t = t * 10 + d
    return t

def play(chooser):
    cur = set(range(1, 10))
    while cur:
        roll = random.randrange(1, 7) + random.randrange(1, 7)
        # print(sorted(list(cur)), roll)
        moves = choices(cur, roll)
        if not moves:
            break
        move = chooser(cur, moves)
        # print("  ", sorted(list(move)))
        cur -= move
    score = calc_score(cur)
    result = sorted(list(cur))
    # print("*", score)
    return score

def choose_random(cur, moves):
    return random.choice(moves)

ngames = 10000

wins = 0
maxs = 0
mins = 123456789
tot = 0
for _ in range(ngames):
    score = play(choose_random)
    if score == 0:
        wins += 1
    mins = min(mins, score)
    maxs = max(maxs, score)
    tot += score

print("wins", wins)
print("min", mins)
print("max", maxs)
print("mean", tot / ngames)
    
