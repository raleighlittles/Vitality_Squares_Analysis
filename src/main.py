import parser
import grapher
import os

if __name__ == "__main__":
    files = parser.discover_files("parsed_data")
    data = []
    for file in files:
        data.append(parser.parse_coordinates(os.path.join("parsed_data", file)))

    grapher.plot_heatmap([item for sublist in data for item in sublist])




