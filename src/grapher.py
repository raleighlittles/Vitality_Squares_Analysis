import matplotlib.pyplot as plt

from typing import List, Tuple

def plot_heatmap(coordinates : List[Tuple[int, int]]):
    x, y = [], []
    for cor in coordinates:
        x.append(cor[1])
        y.append(cor[0])

    fig, ax = plt.subplots()
    ax.set_ylim(3,0)
    ax.grid(True)
    plt.hist2d(x,y, bins=[max(x)+1, max(y)+1], density=True)
    plt.colorbar()
    plt.xticks(range(max(x)))
    plt.yticks(range(max(y)))
    plt.gca().invert_yaxis()
    plt.savefig("myplot.svg")
    plt.close()