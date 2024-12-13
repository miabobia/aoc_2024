from typing import List, Tuple
from copy import deepcopy

def parse(path: str) -> List[List[str]]:
    lines = []
    with open(path, 'r') as f:
        while line := f.readline():
            lines.append(list(line.strip()))
    return lines

def get_starting_pos_and_dir(area: List[List[str]]) -> Tuple[int, int, int]:
    def map_dir(cell: chr) -> int:
        match cell:
            case '^':
                return 0
            case '>':
                return 1
            case 'v':
                return 2
            case '<':
                return 3
        return -1
    
    for i, row in enumerate(area):
        for j, cell in enumerate(row):
            dir = map_dir(cell)
            if dir != -1:
                return (j, i, dir)
    return None

def part_one(area: List[List[str]]) -> int:
    x, y, dir = get_starting_pos_and_dir(area)
    area[y][x] = '&'

    traversed_count = 1

    def get_next_pos(x: int, y: int, dir: int) -> Tuple[int, int]:
        DIR_LOOKUP = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        return (x + DIR_LOOKUP[dir][0], y + DIR_LOOKUP[dir][1])

    while True:
        # get next position
        nx, ny = get_next_pos(x, y, dir)

        # check if next cell is out of bounds (exit condition)
        if nx < 0 or nx >= len(area[0]) or ny < 0 or ny >= len(area[0]):
            break

        # obstacle -> turn and check position again
        if area[ny][nx] == '#':
            dir += 1
            if dir > 3: dir = 0
            continue
        # mark your territory queen
        elif area[ny][nx] != '&':
            traversed_count += 1
        
        # free space -> move forward mark cell
        area[ny][nx] = '&'
        x, y = nx, ny
    return traversed_count

def deepcopy_area(area: List[List[str]]) -> List[List[str]]:
    area_copy = deepcopy(area)
    for row in area:
        area_copy.append(deepcopy(row))
    
    return area_copy

def part_two(area: List[List[str]]) -> int:
    # same as part one but saving guard's direction on each cell she has traversed
    # if the guard has already been in a position and has the same direction we know it's a loop

    loop_count = 0

    for i, row in enumerate(area):
        for j, cell in enumerate(row):
            if area[i][j] in '#^>v<':
                continue
            test_area = deepcopy_area(area)
            test_area[i][j] = '#'
            if test_position_loop(test_area):
                loop_count += 1
    return loop_count

def test_position_loop(area: List[List[str]]) -> bool:
    x, y, dir = get_starting_pos_and_dir(area)
    area[y][x] = [dir]
    visited_hash = {}

    def get_next_pos(x: int, y: int, dir: int) -> Tuple[int, int]:
        DIR_LOOKUP = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        return (x + DIR_LOOKUP[dir][0], y + DIR_LOOKUP[dir][1])

    while True:
        # get next position
        nx, ny = get_next_pos(x, y, dir)

        # check if next cell is out of bounds (exit condition)
        if nx < 0 or nx >= len(area[0]) or ny < 0 or ny >= len(area[0]):
            break

        # obstacle -> turn and check position again
        if area[ny][nx] == '#':
            dir += 1
            if dir > 3: dir = 0
            continue

        # mark your territory queen
        if (nx, ny) not in visited_hash:
            visited_hash[(nx, ny)] = set()
        elif dir in visited_hash.get((nx, ny)):
            return True
        visited_hash[(nx, ny)].add(dir)
        x, y = nx, ny
    return False

if __name__ == '__main__':
    print(f'PART ONE: {part_one(parse('input.txt'))}')
    print(f'PART TWO: {part_two(parse('input.txt'))}')

# yt-dlp
# spotdl
# surface duo