from tkinter import END

import matplotlib.pyplot as plt


def plot_strokes(strokes: list[list[(float, float, float)]]) -> None:
    plt.figure()
    for stroke in strokes:
        stroke = np.array(stroke)
        x = stroke[:, 0]
        y = stroke[:, 1]
        t = stroke[:, 2]
        plt.scatter(x, y)
    plt.gca().set_aspect('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def reset_strokes(strokes, canvas, display):
    strokes.clear()
    canvas.delete("all")
    display.delete(1.0, END)