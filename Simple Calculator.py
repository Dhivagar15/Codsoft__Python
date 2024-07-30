print("SIMPLE CALCULATOR")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
n=int(input("Enter the opeartion you want to perform:"))
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if(n==1):
    sum=num1+num2
    print("Total:",sum)
elif(n==2):
    diff=num1-num2
    print("Difference:",diff)
elif(n==3):
    pro=num1*num2
    print("Product:",pro)
elif(n==4):
    if(num2==0):
        print("ERROR...Division by 0 not possible..!")
    else:
        Quo=num1/num2
        print("Quotient:",Quo)
else:
    print("INVALID..!")
