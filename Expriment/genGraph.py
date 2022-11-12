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
import functools

# number of nodes n1
n1 = 50
k = 10
p = 0.5
mu = 0.5


def get_q(mu, p, k):
    return float((mu * p) / ((1 - mu) * (k - 1)))


def generate_graph(n1=50, k=10, p=0.5, mu=0.3):
    # generate undirected unweighted graph
    # G_P = planted_partition_graph(l=k, k=n1, p_in=p, p_out=get_q(mu, p, k), seed=0)
    G_P = random_partition_graph(
        sizes=[50 for _ in range(10)], p_in=p, p_out=get_q(mu, p, k), seed=0
    )
    print(f"Generated the planted partition graph with size: {len(G_P)}")
    return G_P

    # test the first partion one
    # one_commu = G_P.graph["partition"][0]

def output_graph(G_P):
    # ouput the graph
    with open("Graph.txt", "wb") as f:
        nx.write_edgelist(G_P, f, data=False)

    # output the
    with open("TruthComms.txt", "w") as f:
        for comm in G_P.graph["partition"]:
            f.writelines(" ".join(list(map(lambda x: str(x), comm))))
            f.write("\n")

print("#####################Generate graph############")
G_P = generate_graph(n1=50, k=10, p=0.5, mu=0.3)
output_graph(G_P)
