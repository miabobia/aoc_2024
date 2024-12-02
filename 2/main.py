from typing import List

def parse(path: str) -> List[List[int]]:
    # credit to https://ascii.co.uk/art/walrus for the beautiful walrus :=
    level_rows: List[List[int]] = []
    with open(path, 'r') as f:
        '''
            .-9 9 `\
          =(:(::)=  ;
            ||||     \
            ||||      `-.
           ,\|\|         `,
          /                \
         ;                  `'---.,
         |                         `\
         ;                     /     |
         \                    |      /
          )           \  __,.--\    /
       .-' \,..._\     \`   .-'  .-'
      `-=``      `:    |   /-/-/`
                   `.__/
        '''
        while row := f.readline():
            level_rows.append(list(map(int, row.split())))
    
    return level_rows

def part_one(level_rows: List[List[int]]) -> int:
    safe_levels = 0
    for levels in level_rows:
        increasing = True
        if levels[0] > levels[1]:
            increasing = False

        for i in range(len(levels) - 1):
            diff = levels[i] - levels[i + 1]
            if not diff or abs(diff) > 3:
                safe_levels -= 1
                break         
            
            if diff > 0 and increasing:
                safe_levels -= 1
                break

            if diff < 0 and not increasing:
                safe_levels -= 1
                break

        safe_levels += 1

    return safe_levels

def part_two(level_rows: List[List[int]]) -> int:
    # same as part one with bad_flag to track mistakes
    safe_levels = 0
    for levels in level_rows:
        increasing = True
        if levels[0] > levels[1]:
            increasing = False

        bad_flag = False

        for i in range(len(levels) - 1):
            diff = levels[i] - levels[i + 1]
            if not diff or abs(diff) > 3:
                if bad_flag:
                    safe_levels -= 1
                    break
                bad_flag = True  
            
            if diff > 0 and increasing:
                if bad_flag:
                    safe_levels -= 1
                    break
                bad_flag = True

            if diff < 0 and not increasing:
                if bad_flag:
                    safe_levels -= 1
                    break
                bad_flag = True

        safe_levels += 1

    return safe_levels

if __name__ == '__main__':
    level_input = parse('input.txt')
    print(f'PART ONE: {part_one(level_input)}')
    print(f'PART TWO: {part_two(level_input)}')