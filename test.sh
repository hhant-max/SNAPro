#!/bin/bash
####################generate graph
# python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/genGraph.py -g 'planted' -mu 0.5
python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/genGraph.py -g 'LFR' -mu 0.4
# python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/LFR_graph.txt -g 'LFR' -mu 0.4


#######################get detected comms
cd ./project/localmotif/localmotifcluster || exit

rm -rf outputComu.txt
# ./experimentEvidence -d:Y -i:C-elegans-frontal.txt -m:FFLoop -s:1
#######################get score
./experimentEvidence -d:false -i:/home/sfy/Documents/VScodeProject/SNAPro/Graph.txt -m:UEdge

/home/sfy/miniconda3/envs/sna/bin/python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/getScore.py
