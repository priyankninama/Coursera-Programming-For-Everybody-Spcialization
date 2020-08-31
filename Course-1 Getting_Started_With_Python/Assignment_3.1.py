hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r= float(rate)
except:
    print("Enter Numeric value only")

if h>40:
    reg = r * h
    Out = (h-40.0)*(r*0.5)
    x = reg + Out
else:
    x=h*r
print(x)