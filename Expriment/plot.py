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

# figName = "test.png"

# create result of planted graph # clique3
mu = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
alNamesM = ["MAPPR" for _ in range(9)]
alNamesA = ["APPR" for _ in range(9)]

PF1scoreA = [1.0, 1.0, 0.973, 0.458, 0.337, 0.337, 0.336, 0.326, 0.221]
PF1scoreM = [1.0, 1.0, 1.0, 1.0, 1.0, 0.959, 0.338, 0.333, 0.220]
PtimeM = [0.73, 1.3, 1.6, 2.05, 2.12, 2.98, 4.41, 6.72, 11.1]
PtimeA = [1.1, 1.5, 1.9, 2.1, 2.5, 3.0, 4.4, 6.5, 11.2]

# create result of LFR # clique3
LF1scoreA = [
    1.0,
    0.984,
    0.726,
    0.142,
    0.122,
    0.116,
    0.094,
    0.078,
    0.082
]
LF1scoreM = [1.0, 1.0, 0.998, 0.978, 0.739, 0.303, 0.106, 0.085,0.083]
LtimeM = [1.2, 3.1, 3.4, 3.4, 3.5, 3.4, 3.5, 3.5, 3.3]
LtimeA = [5.0,5.5,5.5,5.7,6.0,6.1,6.4,6.0,6.0]

# result = {
#     "mu": mu,
#     "Algorithms": alNamesM + alNamesA,
#     "F1score": PF1scoreM + PF1scoreA,
#     # "Time(mins)": PtimeM + PtimeA
# }

result = {
    "mu": mu,
    "Algorithms": alNamesM + alNamesA,
    # "F1score": LF1scoreM + LF1scoreA,
    "Time(mins)": LtimeM + LtimeA
}


resultDF = pd.DataFrame(result, columns=["mu", "Algorithms", "Time(mins)"])

# plot
# draw first and then add it
sns.set_theme(style="ticks")
sns.lineplot(
    data=resultDF,
    x="mu",
    y="Time(mins)",
    hue="Algorithms",
    style="Algorithms",
    markers=True,
    dashes=False,
)
# plt.show()
plt.savefig("LFR_time.png")
