#!/bin/bash
python3 /data/s3134644/SNAPro/Expriment/get300Comms.py -i /data/s3134644/SNAPro/dataset/com-amazon.all.dedup.cmty.txt

rm -rf outputComu.txt

./project/localmotif/localmotifcluster/realGraph -d:false -i:/home/sfy/Documents/VScodeProject/SNAPro/dataset/com-lj.ungraph.txt -m:clique3

/home/sfy/miniconda3/envs/sna/bin/python /home/sfy/Documents/VScodeProject/SNAPro/Expriment/getScore.py

/Users/sunfeiyang/miniconda3/envs/sna/bin/python