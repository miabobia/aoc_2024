from typing import List

def parse(path: str) -> List[str]:
    lines = []
    with open(path, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines

def part_one(ws: List[str]) -> int:
    
    def move_valid(move: tuple) -> bool:
        return move[0] >= 0 and move[0] < len(ws)\
        and move[1] >= 0 and move[1] < len(ws[0])

    moves = [
        [(0, 0), (0, -1), (0, -2), (0, -3)], # scan left
        [(0, 0), (0, 1), (0, 2), (0, 3)], # scan down
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)], # scan diagonal up left
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)], # scan diagonal up right
        # [(0, 0), (-1, 1), (-2, 2), (-3, 3)], # scan diagonal down left
        # [(0, 0), (1, 1), (2, 2), (3, 3)] # scan diagonal down right
    ]
    xmas_count = 0
    for y in range(len(ws)):
        for x in range(len(ws[0])):
            for move_list in moves:
                word = ''
                for m in move_list:
                    if not move_valid((m[0]+y, m[1]+x)):
                        break
                    word += ws[m[0]+y][m[1]+x]
                if word == 'XMAS' or word[::-1] == 'XMAS':
                    xmas_count += 1
    return xmas_count

if __name__ == '__main__':
    print(part_one(parse('example.txt')))