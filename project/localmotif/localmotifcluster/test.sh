make clean;
make ;
rm -rf outputComu.txt;
# ./experimentEvidence -d:Y -i:C-elegans-frontal.txt -m:FFLoop -s:1
# ./experimentEvidence -d:false -i:/home/sfy/Documents/VScodeProject/SNAPro/Graph.txt -m:UEdge
./experimentEvidence -d:false -i:/home/sfy/Documents/VScodeProject/SNAPro/Graph_test.txt -m:UEdge
