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
        return G

    if graph == "LFR":
        G = LFR_benchmark_graph(
            1000,
            2.5,
            1.5,
            mu=mu,
            average_degree=20,
            max_degree=50,
            min_community=20,
            max_community=50,
        )
        return G

    # if graph == 'real':
    #     with open(graph_input,'rb') as file:
    #         G = nx.read_edgelist(file)
    #     return G
    # print(f"Generated the planted partition graph with size: {len(G)}")

    # test the first partion one
    # one_commu = G_P.graph["partition"][0]


def output_graph(G, graph):
    # ouput the graph
    with open("Graph.txt", "wb") as f:
        nx.write_edgelist(G, f, data=False)

    # output the
    with open("TruthComms.txt", "w") as f:
        if graph == "planted":
            for comm in G.graph["partition"]:
                f.writelines(" ".join(list(map(lambda x: str(x), comm))))
                f.write("\n")
        if graph == "LFR":
            # for each node
            # for node in G:
            #     # list(G.nodes[i]["community"])
            #     f.writelines(
            #         " ".join(
            #             list(map(lambda x: str(x), list(G.nodes[node]["community"])))
            #         )
            #     )
            #     f.write("\n")

            # for all commnities
            communities = {frozenset(G.nodes[v]["community"]) for v in G}
            for comm in communities:
                f.writelines(" ".join(list(map(lambda x: str(x), comm))))
                f.write("\n")


if __name__ == "__main__":

    # parse the argument
    description = """
    """
    epilog = """

    """
    parser = ArgumentParser(prog="genGraph", description=description, epilog=epilog)

    parser.add_argument(
        "-g", metavar="graph name or dataset name", choices=["planted", "LFR", "real"]
    )
    parser.add_argument("-mu", metavar="mu in planted graph", default=None, type=float)
    # parser.add_argument("-i", metavar="input of real graph",default=None, type=str)

    args = parser.parse_args()
    graph = args.g
    mu = args.mu
    # graph_input = args.i

    #####################Generate graph############

    G_P = generate_graph(graph=graph, mu=mu)
    output_graph(G_P, graph=graph)
