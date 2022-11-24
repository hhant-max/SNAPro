import networkx as nx

import numpy as np

from multicom import load_graph, extract_subgraph
from multicom import approximate_ppr, conductance_sweep_cut
from multicom import multicom
from multicom import load_groundtruth, compute_f1_scores
import time

# real world data

print("Load Amazon data...")
adj_matrix = load_graph(
    "/home/sfy/Documents/testSNA/SNAPro/dataset/com-amazon.ungraph.txt"
)
groundtruth = load_groundtruth("/home/sfy/Documents/testSNA/SNAPro/dataset/A-comms.txt")

print("Filter the nodes with degree 0")
degree = np.array(np.sum(adj_matrix, axis=0))[0]
new_adj_matrix, new_groundtruth, node_map = extract_subgraph(
    adj_matrix, groundtruth, np.where(degree > 0)[0]
)
number_nodes = new_adj_matrix.shape[0]
scoring = lambda adj_matrix, seed_set: approximate_ppr(
            adj_matrix, seed_set, alpha=0.5, epsilon=1e-3
        )
print("Apply MULTICOM on seed node 0")
start = time.time()
# for each node in community
scores_comm = list()
for index_c,comm in enumerate(groundtruth):
    print(f'community {index_c +1}')
    scores_nodes = list()
    for node in comm:
        if node >= number_nodes: continue
        seeds, communities = multicom(
            new_adj_matrix,
            node,
            approximate_ppr,
            conductance_sweep_cut,
            explored_ratio=0.9,
        )
        scores_nodes.append(np.max(compute_f1_scores(communities, new_groundtruth)))
    scores_comm.append(scores_nodes)


print("Compute the average F1-Score for detected communities")
print(f' time spend is {time.time()-start}')
print(np.mean(scores_comm))
