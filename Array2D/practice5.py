# 1
array2D = eval(input())
number = int(input())
for row in range(len(array2D)):
    if len(array2D[0]) <= number:
        array2D = "column error"
    else:
        array2D[row][number] = "*"
print(array2D) 

# # 2
# array2D = eval(input())
# number = int(input())
# for row in range(len(array2D)):
#     if row == number:
#         for col in range(len(array2D[row])):
#             array2D[row][col] = "*"
# print(array2D) 

# # 3
# array = eval(input())
# isFound = True
# for i in range(len(array)):
#     if "X" != array[-1]:
#         if array[i] == "X" and isFound:
#             array[i] = "0"
#             array[i+1] = "X"
#             isFound = False
# print(array)

personsInRoom = eval(input())      # it's an array 2D !
newPersonRow = int(input())        # row of the new person to add
newPersonColumn = int(input())     # column of the new person to add
message = "CAN ADD"
NumberOfPerson = 0  
for row in range(len(personsInRoom)):
    for col in range(len(personsInRoom[row])):
        if personsInRoom[row][col] == 1:
            NumberOfPerson += 1
if NumberOfPerson > 2 or personsInRoom[newPersonRow][newPersonColumn]==1:
    message = "CANNOT ADD"  
print(message)