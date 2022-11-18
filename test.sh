#!/bin/bash
####################generate graph
for mu in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9; do
# for mu in 0.6 0.7 0.8 0.9; do
    echo "----------------Starting mu : ${mu}"
    # python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/genGraph.py -g 'planted' -mu ${mu}
    python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/genGraph.py -g 'LFR' -mu ${mu}
    #######################get detected comms

    rm -rf outputCond.txt
    # ./experimentEvidence -d:Y -i:C-elegans-frontal.txt -m:FFLoop -s:1
    #######################get score
    # ./project/localmotif/localmotifcluster/experimentEvidence -d:false -i:/home/sfy/Documents/VScodeProject/SNAPro/Graph.txt -m:clique3
    ./project/localmotif/localmotifcluster/realGraph -d:false -i:/home/sfy/Documents/VScodeProject/SNAPro/Graph.txt -m:clique3

    /home/sfy/miniconda3/envs/sna/bin/python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/getScore.py

done
