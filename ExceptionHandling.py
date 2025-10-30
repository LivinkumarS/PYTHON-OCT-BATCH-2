# print("Step1")
# print("Step2")
# print("Step3")
# print("Step4")
# print("Step5")


# if 10<90:
#     print("From if block")


# a=10
# b="10"

# print(5/0)

# print("Final Step")


try:
    a=int(input("Enter Your First Number: "))
    b=int(input("Enter Your Second Number: "))
    print("result: ",a/b)
except ZeroDivisionError:
    print("You cannot give 0 as second numbeer!")
except ValueError:
    print("Invalid Input")
finally:
    print("Final Step")


# print(int("you")) 

# print("Final step")