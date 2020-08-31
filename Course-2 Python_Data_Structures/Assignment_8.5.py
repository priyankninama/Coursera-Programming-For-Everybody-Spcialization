fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    # if not line.startswith('From') : continue
    w = line.split()

    if len(w) < 3 or w[0] != 'From':
        continue
    count = count + 1

    print(w[1])

print("There were", count, "lines in the file with From as the first word")
