import numpy as np
import math
import functools


def str2float(strlist):
    strlists = strlist.strip().split(" ")
    ints = list(map(lambda x: float(x), strlists))
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
    detected_comm = str2float(detected_comm)
    conduc = detected_comm[0]

    detected = detected_comm[1:]
    ground_truth_comm = str2float(ground_truth_comm)
    correctly_classified = list(set(detected).intersection(set(ground_truth_comm)))
    precision = len(correctly_classified) / float(len((detected)))
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

    # return [fscore,precision,recall,conduct]
    return [Fscore, precision, recall, conduc]


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
            "/home/sfy/Documents/VScodeProject/SNAPro/outputComu.txt",
            "r",
        )
        .read()
        .strip()
        .split(";")
    )

    statistics = []
    for index, communities in enumerate(detected_communities[:-1]):
        comms_seed = communities.strip().split(",")[:-1]
        # print(comms_seed)
        res = list(
            map(
                functools.partial(
                    cal_Fscore, ground_truth_comm=ground_truth_comm[index], beta=1
                ),
                comms_seed,
            )
        )
        ress = np.array(res).reshape((len(res), 4))
        # res: Fscore,precision,recall,conduc ->[0.3367003367003367, 0.20242914979757085, 1.0, 0.371495]
        # cal score
        max_Fscore_index = np.argmax(ress[:, 0])

        statistics.append(ress[max_Fscore_index])

    result = np.average(statistics, axis=0)
    # mean_best = np.average(statistics) / len()
    # statistics = np.array(statistics)
    # # max_Fscore_index = list(map(np.argmax, statistics[:,:,0]))
    # f = statistics[:,:,0]
    # # max_Fscore_index = np.argmax(statistics[:,:,0])

    # results = [stat[index] for index,stat in zip(max_Fscore_index,statistics)]

    # result = np.average(results,axis=0)
    print(
        f"Fscore:{result[0]:.3f}, Precision:{result[1]:.3f}, Recall:{result[2]:.3f}, Conductance:{result[3]:.3f}"
    )
