import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# create result
mu = [0.05,]
alNamesM = ["MAPPR" for _ in range(10)]
alNamesA = ["APPR" for _ in range(10)]
F1scoreM = [0.964743162439931,]
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
