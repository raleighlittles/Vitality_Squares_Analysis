import src.parser
import src.grapher
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("i", help="Input directory: where Vitality Squares data is stored.", type=str)
    args = parser.parse_args()

    files = src.parser.discover_files(args.i)

    data = []
    for file in files:
        data.append(src.parser.parse_coordinates(os.path.join(args.i, file)))

    src.grapher.plot_heatmap([item for sublist in data for item in sublist])
