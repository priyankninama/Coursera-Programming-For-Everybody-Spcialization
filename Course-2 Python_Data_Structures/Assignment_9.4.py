name = input("Enter file:")
fname = open(name)
di = {}

for line in fname:
    if line.startswith("From "):
        w = line.split()
        wd = w[1]
        di[wd] = di.get(wd, 0) + 1

large = 0
theword = None

for k, v in di.items():
    if v > large:
        large = v
        theword = k

print(theword, large)