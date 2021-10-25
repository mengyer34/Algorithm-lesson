# # 1
# array2D = eval(input())
# message = "lost"
# for row in range(len(array2D)):
#     found7 = 0
#     for col in range(len(array2D[row])):
#         if array2D[row][col] == 7:
#             found7 += 1
#     if found7 == 3:
#         message = "win"
# print(message)

# #2
# firstArr2D = eval(input())
# secondArr2D = eval(input())
# message = "equal"
# checkValue = 0 
# numberOfElement = 0 
# if len(firstArr2D) == len(secondArr2D):
#     for row in range(len(firstArr2D)):
#         for col in range(len(firstArr2D[row])):
#             if firstArr2D[row][col] == secondArr2D[row][col]:
#                 checkValue += 1
#                 numberOfElement += 1
# if checkValue != numberOfElement:
#     message = "not equal"
# print(message) 

# 3 
def signOnRow(grid, rowIndex, sign):
    for row in range(len(grid[rowIndex])):
        if sign != grid[row][rowIndex]:
            return False       
    return True 
  
def signOnColumn(grid, columnIndex, sign):
    for col in range(len(grid[columnIndex])):
        if sign != grid[columnIndex][col]:
            return False
    return True
        
def signOnDiagonal(grid, sign):
    if grid[0][0] == sign and grid[1][1] == sign and grid[2][2] == sign:
        return True
    elif grid[0][2] == sign and grid[1][1] == sign and grid[2][0] == sign:
        return True
    return False

def hasSignWon(grid, sign):
    for i in range(len(grid)):
        if signOnDiagonal(grid, sign) or signOnColumn(grid, i, sign) or signOnRow(grid, i, sign):
            return True
    return False

grid = eval(input())
if hasSignWon(grid, "A"):
    print("A WON")

elif hasSignWon(grid, "B"):
    print("B WON")

else:
    print("NO WINNER")