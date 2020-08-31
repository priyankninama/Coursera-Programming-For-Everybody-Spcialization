fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    v = line.rstrip()
    p = line.split()

    for x in p:
        if x not in lst:
            lst.append(x)

lst.sort()
print (lst)
