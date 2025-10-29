# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")

# printSteps()
# printSteps()
# printSteps()

# print(12)
# print(33)
# input()
# int()

# def findSum(a,b,c=10):
#     print(a+b+c)

# findSum(3,4,5)
# findSum(33,44,55)

# findSum(b=3,a=4,c=5)

# findSum(3,4)

# def steps():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("Step4")
#     return [1,2,3,4,5]
    
# ans=steps()
# print(ans)

# def findSum(a,b,c):
#     return a+b+c

# print(findSum(1,2,3))

# def findProduct(a,b):
#     return a*b

# print(findProduct(2,findProduct(4,findProduct(3,2))))

a=15

def dummy():
    a=10 #(local overrides global)
    print("A's value from inside the function: ",a)

dummy()
print("A's value from outside the function: ",a)