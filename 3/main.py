import re
from enum import Enum
from dataclasses import dataclass

class ComputerState(Enum):
    DO = 1
    DONT = 2

@dataclass
class Computer:
    state = ComputerState.DO
    sum = 0
    
    def execute_instruction(self, instruction: str):
        if self.state == ComputerState.DO and instruction.startswith("mul"):
            a, b = map(int, filter(None, re.findall(r'\d*', instruction)))
            self.sum += a * b
        elif instruction.startswith("don't"):
            self.state = ComputerState.DONT
        elif instruction.startswith("do"):
            self.state = ComputerState.DO

    def reset(self):
        self.sum = 0
        self.state = ComputerState.DO

def parse_input(path: str) -> str:
    s: str
    with open(path, 'r') as f:
        s = f.read()    
    return s

def part_one(input: str, toboggan_computer: Computer) -> int:
    pattern = r'mul[(]\d*,\d*[)]'
    for instruction in re.findall(pattern, input):
        toboggan_computer.execute_instruction(instruction)

def part_two(input: str, toboggan_computer: Computer) -> int:
    pattern = r"mul[(]\d*,\d*[)]|don't|do"
    for instruction in re.findall(pattern, input):
        toboggan_computer.execute_instruction(instruction)

if __name__ == '__main__':
    # 🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷🖥️🛷
    toboggan_computer = Computer()
    instructions = parse_input("input.txt")

    part_one(instructions, toboggan_computer)
    print(f'PART ONE: {toboggan_computer.sum}')

    toboggan_computer.reset()

    part_two(instructions, toboggan_computer)
    print(f'PART TWO: {toboggan_computer.sum}')