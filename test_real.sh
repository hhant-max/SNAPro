#!/bin/bash
/home/sfy/miniconda3/envs/sna/bin/python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/get100Comms.py -i /home/sfy/Documents/VScodeProject/SNAPro/dataset/com-lj.all.cmty.txt

rm -rf outputComu.txt

./project/localmotif/localmotifcluster/realGraph -d:false -i:/home/sfy/Documents/VScodeProject/SNAPro/dataset/com-lj.ungraph.txt -m:clique3

/home/sfy/miniconda3/envs/sna/bin/python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/getScore.py

/Users/sunfeiyang/miniconda3/envs/sna/bin/python

# for server
/data/s3134644/SNAPro/project/localmotif/localmotifcluster/realGraph -d:false -i:/data/s3134644/SNAPro/dataset/com-lj.ungraph.txt -m:UEdge

python /data/s3134644/SNAPro/Expriment/getScore.py