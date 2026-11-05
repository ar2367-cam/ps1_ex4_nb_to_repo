from contextlib import contextmanager

import matplotlib.pyplot as plt
import seaborn as sns

from titanic.config import COLOR_LIST, FIGURES_DIR


def _colours(df, hue):
    """Seaborn colour arguments: one colour per hue level, or a single colour."""
    if hue:
        return {"hue": hue, "palette": COLOR_LIST[: df[hue].nunique()]}
    return {"color": COLOR_LIST[1]}


def plot_counts(df, column, hue=None):
    """Bar chart of how many rows have each value of column, optionally split by hue."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(x=column, data=df, ax=ax, **_colours(df, hue))
    ax.grid(color="black", linestyle="-.", linewidth=0.5, axis="y", which="major")
    ax.set_title(f"Number of passengers / {column}")
    plt.show()


def plot_distribution(df, column, hue=None):
    """Histogram of column, optionally split by hue."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(data=df, x=column, ax=ax, **_colours(df, hue))
    ax.set_title(f"Distribution of {column}")
    plt.show()


@contextmanager
def save_figure(filename):
    """Save the figure drawn inside the with-block to figures/<filename>, just before it is shown."""
    original_show = plt.show

    def show_and_save(*args, **kwargs):
        FIGURES_DIR.mkdir(exist_ok=True)
        plt.gcf().savefig(FIGURES_DIR / filename, dpi=150, bbox_inches="tight")
        original_show(*args, **kwargs)

    plt.show = show_and_save
    try:
        yield
    finally:
        plt.show = original_show
