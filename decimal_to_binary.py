num = int(input("Enter a decimal number: "))
b = ""  
while num > 0:
    remn = num % 2         
    b = str(remn) + b 
    num = num // 2              
if b == "":
    b= "0"
print("Binary ", b)