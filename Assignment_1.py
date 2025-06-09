n = int(input("Enter the number of rows: "))

def lower_triangle(n):
    print("\nLower Triangle: ")
    for i in range(1, n+1):
        print("* " * i)
        
def upper_triangle(n):
    print("\nUpper Triangle: ")
    for i in range(n,0,-1):
        print("* "* i)
        
def pyramid(n):
    print("\nPyramid Pattern: ")
    for i in range(1, n+1):
        spaces = ' ' *(n-i)
        stars = '* '*i
        print(spaces + stars)
        
lower_triangle(n)
upper_triangle(n)
pyramid(n)