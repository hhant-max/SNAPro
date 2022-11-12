import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# create result
mu = np.arange(0, 1, 0.1)
alNamesM = ["MAPPR" for _ in range(10)]
alNamesA = ["APPR" for _ in range(10)]
F1scoreM = [...]
F1scoreA = [...]
figName = "test.png"


result = {
    "mu": mu,
    "algorithms": alNamesM + alNamesA,
    "F1score": F1scoreM + F1scoreA,
}

resultDF = pd.DataFrame(result, columns=["mu", "algorithms", "F1score"])

# plot
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
