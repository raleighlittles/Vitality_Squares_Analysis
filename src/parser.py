import os
import re
from typing import List

def discover_files(root_dir : str):
    return [file for file in os.listdir(root_dir) if file.endswith(".txt")]

def extract_results_from_text(input_file_for_month : str) -> List[str]:
    coords_of_fruits = []
    for coordinates in input_file_for_month.split("\n"):
        coords_of_fruits.append(tuple(map(int, re.sub('\W', '', coordinates))))
    return coords_of_fruits