def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2
    
def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2 
    #ok

def mod(num1,num2):
    return num1%num2

print("Select any option")
print("1.Addition")
print("2.subtract")
print("3.Multiplication")
print("4.division")
print("5.modulus")

operation=int(input("select any operation from 1,2,3,4,5:"))

number_1=int(input("enter one number:"))
number_2=int(input("enter another number:"))

if operation==1:
    print(number_1, "+", number_2, "=",add(number_1, number_2))
elif operation==2:
    print(number_1, "-", number_2, "=",sub(number_1, number_2))
elif operation==3:
    print(number_1, "*", number_2, "=",mul(number_1, number_2))
elif operation==4:
    print(number_1, "/", number_2, "=",div(number_1, number_2))
elif operation==5:
    print(number_1, "%", number_2, "=",mod(number_1, number_2))
else:
    print("invalid operation")

