import numpy as np
import math
import functools

def str2int(strlist):
    strlists = strlist.strip().split(" ")
    ints = list(map(lambda x: int(x), strlists))
    return ints



def cal_Fscore(detected_comm, ground_truth_comm, beta=1):
    """
    input : detected_comm: list from read file wiht all str
            ground_truth_comm: list with community of int

    Given a set of algorithmic communities C and the ground truth communities S, F score measures the relevance
    between the algorithmic communities and the ground truth communities.
    F_beta = (1+beta^2) / beta^2 * (precision(S)*recall(S)) / (precision(S)+recall(S))
    """
    # input detected_comm = '0 3 4 2 6 ... ' transfer first
    detected_comm = str2int(detected_comm)
    ground_truth_comm = str2int(ground_truth_comm)
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


def cal_Jaccard(detected_comm, ground_truth_comm):
    """
    Jaccard is defined as the size of the intersection divided by the size of the union of the sample sets

    """
    detected_comm_ = detected_comm.strip().split(" ")
    detected_comm = list(map(lambda x: int(x), detected_comm_))
    ground_truth_comm = list(ground_truth_comm)
    correctly_classified = list(set(detected_comm).intersection(set(ground_truth_comm)))
    union = list(set(detected_comm).union(set(ground_truth_comm)))
    Jind = len(correctly_classified) / float(len(union))

    return Jind


if __name__ == "__main__":

    #####################calcualte F1 score############
    # singleFscore = cal_Fscore(detected_comm= detected_comm,ground_truth_comm=one_commu)

    # read graound truth commuities
    ground_truth_comm = list(
        open(
            "/home/sfy/Documents/VScodeProject/SNAPro/TruthComms.txt",
            "r",
        )
        .read()
        .strip()
        .split("\n")
    )

    # read detected communities from file
    detected_communities = list(
        open(
            "/home/sfy/Documents/VScodeProject/SNAPro/project/localmotif/localmotifcluster/outputComu.txt",
            "r",
        )
        .read()
        .strip()
        .split(";")
    )

    scoress = []
    for index, communities in enumerate(detected_communities[:-1]):
        comms_seed = communities.strip().split(",")[:-1]
        # print(comms_seed)
        scores = list(
            map(
                functools.partial(
                    cal_Fscore, ground_truth_comm=ground_truth_comm[index], beta=1
                ),
                comms_seed,
            )
        )
        scoress.append(scores)

    # mean_best = np.average(scoress) / len()
    mean_best = np.average(list(map(np.max, scoress)))

    print(mean_best)
