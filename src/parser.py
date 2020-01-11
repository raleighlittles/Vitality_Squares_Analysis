import os
import ast
import pdb
from typing import List


def discover_files(root_dir: str) -> List[str]:
    return [file for file in os.listdir(root_dir) if file.endswith(".txt")]

def parse_coordinates(input_file_for_month: str):
    coords_of_fruits = []
    with open(input_file_for_month, 'r') as file:
        for line in file:
                if line.rstrip():
                    coords_of_fruits.append(ast.literal_eval(line))

    return coords_of_fruits
