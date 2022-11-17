from itertools import islice

with open("/home/sfy/Documents/VScodeProject/SNAPro/dataset/com-dblp.top5000.cmty.txt", "r") as myfile:
    head = list(islice(myfile, 100))

# always remember, use files in a with statement
with open("TruthComms.txt", "w") as f2:
    for item in head:
        f2.write(item)