import re
from enum import Enum
from dataclasses import dataclass

class StateType(Enum):
    DO = 1
    DONT = 2

@dataclass
class Computer:
    state = StateType.DO
    sum = 0
    
    def execute_instruction(self, instruction: str):
        if instruction.startswith("mul") and self.state == StateType.DO:
            a, b = map(int, re.split(r'[(,)]', instruction)[1:3])
            self.sum += a * b
        elif instruction.startswith("don't"):
            self.state = StateType.DONT
        elif instruction.startswith("do"):
            self.state = StateType.DO

    def reset(self):
        self.sum = 0
        self.state = StateType.DO

def parse_input(path: str) -> str:
    s: str
    with open(path, 'r') as f:
        s = f.read()    
    return s

def part_one(input: str, toboggan_computer: Computer) -> int:
    pattern = r'mul[(]\d*,\d*[)]'
    for match in re.findall(pattern, input):
        toboggan_computer.execute_instruction(match)

def part_two(input: str, toboggan_computer: Computer) -> int:
    pattern = r"mul[(]\d*,\d*[)]|don't|do"
    for match in re.findall(pattern, input):
        print(f'sending instruction {match}')
        toboggan_computer.execute_instruction(match)

if __name__ == '__main__':
    # 🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷
    toboggan_computer = Computer()
    instructions = parse_input("input.txt")

    part_one(instructions, toboggan_computer)
    print(f'PART ONE: {toboggan_computer.sum}')

    toboggan_computer.reset()

    part_two(instructions, toboggan_computer)
    print(f'PART TWO: {toboggan_computer.sum}')