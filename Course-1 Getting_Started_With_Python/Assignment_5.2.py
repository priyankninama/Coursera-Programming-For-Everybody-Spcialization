large = None
small = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" :
            break
        num= int(num)
        if large is None or large < num:
            large=num
        elif small is None or small>num:
            small = num
    except:
        print("Invalid input")

print("Maximum is", large)
print("Minimum is", small)