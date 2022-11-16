import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# create result
mu = [0.3,0.4,0.5,0.7,0.8]
alNamesM = ["MAPPR" for _ in range(10)]
alNamesA = ["APPR" for _ in range(10)]
F1scoreM = [0.9690543190560558,0.3993207861247067,0.33681561366125123,0.33613767820070706,0.3253332962958847]
F1scoreA = [...]
figName = "test.png"


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
