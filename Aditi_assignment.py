units = int(input("Enter units consumed: "))
if units<=100:
    bill = units*1
elif units <=300:
    bill=100+(units-100)*1.25
elif units <=500:
    bill=350+(units-300)+1.50
else:
    bill=650+(units-500)*1.75
print("electricity Bill = Rs.",bill)