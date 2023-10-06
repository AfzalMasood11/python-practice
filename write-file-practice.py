# For writing in a file:
# with open('test.txt', 'w') as file:
#     file.write("It is sample text to write in a file")

# alternate way, also with append flag:
file = open('test.txt', 'a')
file.write('Second, line')
file.close


# ################# #
# for reading

with open('test.txt', 'r') as file:
    line = file.read()
    print(line)