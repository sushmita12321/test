# Write a pythone functionto find the Max of three numbers.
def max(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
x = float(input("enter a first no."))
y = float(input("enter a second no."))
z = float(input("enter a third no."))
print("greatest no.among the three no is ",max(x,y,z))