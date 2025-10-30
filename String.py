a="hello guys hi hi hi"

# print('He' not in a)
# print(len([1,2,3,4,5]))

# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.capitalize())
# print(a.count('h'))
# print(a.find('x'))
# print(a.replace('hi','good morning'))



# lis1=a.split(' ')
# print(lis1)

# lis=['hello', 'guys', 'hi', 'hi', 'hi']
# print(' '.join(lis))

# c="hello world     "

# c[3]='x'

# print(c)

# b="1123"

# print(c)
# print(c.strip())

# print(b.isalpha())
# print(b.isdigit())


# name="hendry"
# role="dev"
# age=40

# print(f'I am {name}. Role is {role}. {age} years old!')

# palindrome or not?
# input
# a=input("Enter the string")
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")


a = input("Enter a string: ")
text= a.lower()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")