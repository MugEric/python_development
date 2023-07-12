

# Verify the Given Number is Positive or not
val= int(input("Enter a number: "))

if val % 2 == 0:
    print("Even")
else:
    print("Odd")   

# with function 

def verify_Even(val): 
    if val % 2 == 0:
        return "Even", val
    else: 
        return "Odd", val

val = int(input("provide a number to check if its odd or Even"))
msg, value = verify_Even(val)
print(msg, value)

#Class Function 

class Exercise2:
    def verify_Even(val):
        if val % 2 == 0:
            return "Even", val
        else: 
            return "Odd", val

val = int(input("Enter a number to check if its odd or Even"))
msg, value = Exercise2.verify_Even(val)
print(msg, val)