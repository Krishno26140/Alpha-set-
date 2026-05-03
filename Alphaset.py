# Funtion to compute the Alpha_LEvel set (AlPHA - cut )
# this funtion contain the core filteriing logic of the program 
# it recives: 1. arr -> list of fuzzy  membership values   2. alpha -> threshold value used for filtering 
def alpha_set(arr: list, alpha: float):
    # heading for output display 
    print("Alpha_level_set: " )
    # transverse everything  membership value in the fuzzy set 
    # sequential traversal allows checking each value individually for i in arr:

    for i in arr:
        # core filtering logic condition of alpha-cut theory 
        # only values greater than alpha or greater than alpha are accepted  
        if i > alpha:
            print(i)

A1: list = []
# user specifies how many membership values will be entered 

n: int = int(input("Enter number of elements: "))
# loop executes n times to collect fuzzy membership values  for i in range (n)
for i in range(n):

    value: float  = float(input("Enter the values: "))
    A1.append(value)

alpha: float = float(input("Enter the value of alpha: "))
# funtion call:
# sends both the fuzzy set aplha threshold into the funtion 
# the funtion then processes the list and generates the alpha_ level set 
alpha_set(A1, alpha)