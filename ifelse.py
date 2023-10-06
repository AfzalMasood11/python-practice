# age = int(input("Enter your age"))

# if(age >= 18):
#     print("19It is in inside If section")
# elif(age > 5 and age < 17):
#     print('You are a kid')
# else:
#     print('inside Else')

#  Else is not required.


##### Match 
a = 2
match a:
    case 1:
        print('it is case1')
    case 2:
        print('it is case2')
    case _:
        print("Its a DEFAULT CASE")