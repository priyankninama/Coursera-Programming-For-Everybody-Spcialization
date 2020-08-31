name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = {}

for line in handle:
    if line.startswith("From ") and len(line.split())>2:
        wds = line.split()
        if not di.has_key(wds[5][:2]):
            di[wds[5][:2]] = 1
        else:
           di[wds[5][:2]] += 1

key=sorted(di)
for i in key:
    print (i,di[i])