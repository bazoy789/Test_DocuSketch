import matplotlib.pyplot as plt
import pandas as pd
import os

count_file = 0


def save_file(figure):
    global count_file
    folder = os.listdir(".")
    if "plots" not in folder:
        os.mkdir("./plots")
    else:
        pass
    figure.savefig(f"./plots/plot{count_file}.png")
    count_file += 1


def plot_comparing(data: pd.DataFrame, *columns):
    fig, ax = plt.subplots()

    fig.set_figheight(5)
    fig.set_figwidth(10)

    for column in columns:
        ax.plot(data[column], label=column, alpha=1)

    plt.legend()
    plt.title([head for head in columns])

    plt.show()

    save_file(fig)


def draw_plots(file):

    data = pd.read_json(file)

    data["check_prediction"] = data["gt_corners"] - data["rb_corners"]

    main_figure = data.plot(y="check_prediction", grid=True, linestyle='--', alpha=1).get_figure()
    save_file(main_figure)

    plot_comparing(data, "mean", "max", "min")
    plot_comparing(data, "floor_mean", "floor_max", "floor_min")
    plot_comparing(data, "ceiling_mean", "ceiling_max", "ceiling_min")


if __name__ == "__main__":
    draw_plots("data.json")
    print("File to create")
else:
    print("File not to create")
