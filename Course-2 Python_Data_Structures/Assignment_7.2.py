total = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x = line.split()
    w = (x[1])
    s = float(w)
    total = total + s
    count = count + 1
average = total/count
print('Average spam confidence:',average)
