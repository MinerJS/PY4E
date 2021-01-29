hrs = input("Enter Hours:")
h = float(hrs)
rate= input("Enter Pay rate per hours:")
r = float(rate)
if h <= 40:
    p=h*r
    print(p)
else:
    p=r*40
    e=r*1.5*(h-40)
    print(p+float(e))
