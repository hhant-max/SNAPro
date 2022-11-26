from itertools import islice
import os
from argparse import ArgumentParser

# ╰─➤  /home/sfy/miniconda3/envs/sna/bin/python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/get100Comms.py -file '/home/sfy/Documents/VScodeProject/SNAPro/dataset/com-dblp.ungraph.txt'

parser = ArgumentParser(prog="gen300Comms")
parser.add_argument("-i", metavar="file name of original comms", type=str)
args = parser.parse_args()
# print(args.file)
# os.path.dirname(__file__) Experiment
# get os.getcwd() -> SNAPRO

with open(args.i, "r") as myfile:
    head = list(islice(myfile, 300))

# always remember, use files in a with statement
with open(os.path.join(os.getcwd(), "TruthComms.txt"), "w") as f2:
    for item in head:
        f2.write(item)
