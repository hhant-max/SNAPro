#!/bin/bash
####################generate graph
python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/genGraph.py -g 'planted' -mu 0.99

#######################get detected comms
cd ./project/localmotif/localmotifcluster || exit
make clean
make
rm -rf outputComu.txt
# ./experimentEvidence -d:Y -i:C-elegans-frontal.txt -m:FFLoop -s:1
#######################get score
./experimentEvidence -d:false -i:/home/sfy/Documents/VScodeProject/SNAPro/Expriment/Graph.txt -m:UEdge

/home/sfy/miniconda3/envs/sna/bin/python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/getScore.py
