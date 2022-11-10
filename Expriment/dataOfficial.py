import numpy as np
import networkx as nx
from networkx.generators.community import (
    LFR_benchmark_graph,
    planted_partition_graph,
    random_partition_graph,
)
from networkx.algorithms import community
import os
import math

# number of nodes n1
n1 = 50
k = 10
p = 0.5
mu = 0.5


def get_q(mu, p, k):
    return float((mu * p) / ((1 - mu) * (k - 1)))


# generate undirected unweighted graph
# G_P = planted_partition_graph(l=k, k=n1, p_in=p, p_out=get_q(mu, p, k), seed=0)
G_P = random_partition_graph(
    sizes=[50 for _ in range(10)], p_in=p, p_out=get_q(mu, p, k), seed=0
)
print(f"Generated the planted partition graph with size: {len(G_P)}")

# test the first partion one
# one_commu = G_P.graph["partition"][0]

# ouput the graph
with open("Experiment_Graph.txt", "wb") as f:
    nx.write_edgelist(G_P, f, data=False)

# output the
with open("groundTruthCom.txt", "w") as f:
    for comm in G_P.graph["partition"]:
        f.writelines(" ".join(list(map(lambda x: str(x), comm))))
        f.write("\n")

# read from txt
with open(
    "/home/sfy/Documents/VScodeProject/SNAPro/project/localmotif/localmotifcluster/outputComu.txt",
    "r",
) as f:
    detected_comm = list(f.read().strip().split(" "))

    # compare with F1score


def cal_Fscore(detected_comm, ground_truth_comm, beta=1):
    """
    input : detected_comm: list from read file wiht all str
            ground_truth_comm: list with community of int

    Given a set of algorithmic communities C and the ground truth communities S, F score measures the relevance
    between the algorithmic communities and the ground truth communities.
    F_beta = (1+beta^2) / beta^2 * (precision(S)*recall(S)) / (precision(S)+recall(S))
    """
    detected_comm = list(map(lambda x: int(x), detected_comm))
    ground_truth_comm = list(ground_truth_comm)
    print(ground_truth_comm)
    correctly_classified = list(set(detected_comm).intersection(set(ground_truth_comm)))
    precision = len(correctly_classified) / float(len((detected_comm)))
    recall = len(correctly_classified) / float(len(ground_truth_comm))
    if precision != 0 and recall != 0:
        Fscore = (
            (1 + math.sqrt(beta))
            / float(math.sqrt(beta))
            * precision
            * recall
            / float(precision + recall)
        )
    else:
        Fscore = 0

    return Fscore

print('#####################calcualte F1 score############')
singleFscore = cal_Fscore(detected_comm= detected_comm,ground_truth_comm=one_commu)
