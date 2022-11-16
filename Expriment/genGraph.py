import numpy as np
import networkx as nx
from networkx.generators.community import (
    LFR_benchmark_graph,
    random_partition_graph,
    planted_partition_graph,
)
from networkx.algorithms import community
from argparse import ArgumentParser


def get_q(mu, p, k):
    return float((mu * p) / ((1 - mu) * (k - 1)))


def generate_graph(graph, mu):
    # generate undirected unweighted graph
    if graph == "planted":
        # number of nodes n1
        n = 50
        k = 10
        p = 0.5
        mu = mu

        # G = random_partition_graph(
        #     sizes=[n for _ in range(k)], p_in=p, p_out=get_q(mu, p, k), seed=0
        # )
        G = planted_partition_graph(
            l=10, k=50, p_in=0.5, p_out=get_q(mu=mu, p=0.5, k=10)
        )

    if graph == "LFR":
        G = LFR_benchmark_graph()
    # TODO: real datasets

    print(f"Generated the planted partition graph with size: {len(G)}")
    return G

    # test the first partion one
    # one_commu = G_P.graph["partition"][0]


def output_graph(G_P, graph):
    # ouput the graph
    with open("Graph.txt", "wb") as f:
        nx.write_edgelist(G_P, f, data=False)

    # output the
    with open("TruthComms.txt", "w") as f:
        if graph == "planted":
            for comm in G_P.graph["partition"]:
                f.writelines(" ".join(list(map(lambda x: str(x), comm))))
                f.write("\n")


if __name__ == "__main__":

    # parse the argument
    description = """
    """
    epilog = """

    """
    parser = ArgumentParser(prog="genGraph", description=description, epilog=epilog)

    # TODO: add real world datasets here
    parser.add_argument(
        "-g", metavar="graph name or dataset name", choices=["planted", "LFR"]
    )
    parser.add_argument("-mu", metavar="mu in planted graph", type=float)

    args = parser.parse_args()
    graph = args.g
    mu = args.mu

    #####################Generate graph############

    G_P = generate_graph(graph=graph, mu=mu)
    output_graph(G_P, graph=graph)
