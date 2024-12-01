from typing import List
from collections import Counter

def parse(path: str) -> List[tuple]:
    location_ids: List[tuple]
    with open(path, 'r') as f:
        location_ids = list(map(tuple, map(lambda x: x.split(), f.readlines())))

    return location_ids

def part_one(locs: List[tuple]) -> int:
    left_locs = sorted([int(l[0]) for l in locs], reverse=True)
    right_locs = sorted([int(l[1]) for l in locs], reverse=True)

    return sum([abs(a - b) for a, b in zip(left_locs, right_locs)])

def part_two(locs: List[tuple]) -> int:
    sim_score = 0
    right_freq = Counter([int(l[1]) for l in locs])
    for loc in [int(l[0]) for l in locs]:
        sim_score += loc * right_freq[loc]

    return sim_score

if __name__ == '__main__':
    locations = parse('input.txt')
    print(f'PART ONE: {part_one(locations)}')
    print(f'PART TWO: {part_two(locations)}')