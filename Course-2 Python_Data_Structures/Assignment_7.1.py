# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for fx in fh:
    fy = fx.rstrip()
    print(fy.upper())