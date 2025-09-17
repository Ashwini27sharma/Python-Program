cp=float(input ("enter the cost price: "))
sp=float(input("enter the selling price: "))
res = sp-cp
if res<0:
    print("Its loss")
elif res >0:
    print("Its profit")
else:
    print('Neither profit nor loss')