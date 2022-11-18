import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# distract result from output
# result = list(
#     open(
#         "/home/sfy/Documents/VScodeProject/SNAPro/output.txt",
#         "r",
#     )
#     .read()
#     .strip()
#     .split("Starting mu : 0.1")
# )

figName = "test.png"

# create result of planted graph # clique3
mu = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
alNamesM = ["MAPPR" for _ in range(10)]
alNamesA = ["APPR" for _ in range(10)]

PF1scoreA = [1.0, 1.0, 0.973, 0.458, 0.337, 0.337, 0.336, 0.326, 0.221]
PF1scoreM = [1.0, 1.0, 1.0, 1.0, 1.0, 0.959, 0.338, 0.333, 0.220]
PtimeM = [0.73, 1.3, 1.6, 2.05, 2.12, 2.98, 4.41, 6.72, 11.1]
PtimeA = [1.1, 1.5, 1.9, 2.1, 2.5, 3.0, 4.4, 6.5, 11.2]

# create result of LFR # clique3
LF1scoreA = [
    0.9690543190560558,
    0.3993207861247067,
    0.33681561366125123,
    0.33613767820070706,
    0.3253332962958847,
]
LF1scoreM = [1.0, 1.0, 0.1, 0.1, 0.958, 0.338, 0.333, 0.220]
LtimeM = [0.73, 1.3, 1.6, 2.05, 2.12, 2.98, 4.41, 6.72, 11.1]
LtimeA = []


result = {
    "mu": mu,
    "algorithms": alNamesM + alNamesA,
    "F1score": F1scoreM + F1scoreA,
}

resultDF = pd.DataFrame(result, columns=["mu", "algorithms", "F1score"])

# plot
# draw first and then add it
sns.set_theme(style="ticks")
sns.lineplot(
    data=resultDF,
    x="mu",
    y="F1score",
    hue="algorithms",
    style="algorithms",
    markers=True,
    dashes=False,
)

plt.savefig(figName)
