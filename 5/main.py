from typing import List

def parse(path: str) -> List[str]:
    rules = []
    updates = []
    current = rules
    with open(path, 'r') as f:
        for line in map(lambda x: x.strip(), f.readlines()):
            if line == '':
                current = updates
            else:
                current.append(line)
    
    return rules, updates

def part_one(rules: List[str], updates: List[str]) -> int:
    rule_hash = {}

    # create rules
    for a, b in map(lambda x: x.split('|'), rules):
        rule_hash.setdefault(a, set()).add(b)

    middle_pages_sum = 0

    # check rules on updates
    for update in updates:
        pages = update.split(',')
        good_update = True
        for i in range(len(pages)-1, 0, -1):
            current_page = pages[i]
            prev_pages = set(pages[0:i])
            if not (current_page not in rule_hash or rule_hash[current_page].isdisjoint(prev_pages)):
                good_update = False
                break
        if good_update: middle_pages_sum += int(pages[len(pages)//2])
    
    return middle_pages_sum

if __name__ == '__main__':
    rules, updates = parse('input.txt')
    print(f'PART ONE: {part_one(rules, updates)}')