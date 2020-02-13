# Write a pythone script to generate and print a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample Dictionary(n=5):
# Expected output : {1:1,2:4,3:9,4:16,5:25}
square = {}
for x in range(1,6,1):
    square[x] = x*x
    print(square)

