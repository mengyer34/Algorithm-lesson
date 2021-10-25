# Converth to function


# def takeAllChar(array2D):
#     for row in range(len(array2D)):
#         rows = array2D[row]
#         for col in range(len(rows)):
#     return array2D



# #1
# words = ["hello","ill"]
# # words = eval(input())
# result = []
# for i in range(len(words)):
#     arr = []
#     word = words[i]
#     for j in range(len(word)):      
#         arr.append(word[j].upper())
#     result.append(arr)
# print(result)

# # or
# def transferCharToArray2D(arry):
#     result = []
#     for row in range(len(arry)):
#         rows = arry[row]
#         arr = []
#         for col in range(len(rows)):
#             arr.append(rows[col].upper())
#         result.append(arr)
#     return result
# array = ["hello","ill"]
# print (transferCharToArray2D(array))



# # 2 
# # array = eval(input())
# array = [
#     [1,5,0],
#     [2,3,1],
#     [9,5,2]
#     ]

# result = []
# for i in array: 
#     max = 0
#     for j in range(len(i)):      
#         if i[j] > max:
#             max = i[j]
#     result.append(max)
# print(result)

# # or 
# def findMaxNumArr2D(array2D):
#     result = []  
#     for row in array2D:
#         max = 0
#         for col in range(len(row)):
#             if row[col] > max:
#                 max = row[col]
#         result.append(max)
#     return result

# array2D = eval(input())  
# print(findMaxNumArr2D(array2D))


# # 3
# array2D = [
#     [1,4,3,4],
#     [1,8,3,4],
#     [7,0,5,0]
# ]

# result = []
# for col in range(len(array2D)):
#     cols = array2D[col]
#     for row in range(len(cols)):
#         if cols[row] == 7:
#             result.append(col)
#             result.append(row)
# print(result)

# or 

# def findIndexOfRowNCol(array2D):
#     result = []
#     for col in range(len(array2D)):
#         cols = array2D[col]
#         for row in range(len(cols)):
#             if cols[row] == 7:
#                 result.append(col)
#                 result.append(row)
#     return result
# array2D = eval(input())
# print(findIndexOfRowNCol(array2D))

# 4
# array2D = [
#     [7,4,3,4],
#     [1,7,3,4],
#     [7,0,5,7]
# ]
# for col in range(len(array2D)):
#     cols = array2D[col]
#     for row in range(len(cols)):
#         if cols[row] == 7:
#             cols[row] = 8
# print(array2D)


# 5
def changeChar(array2D, number):
    for row in array2D:
        for col in range(len(row)):
            if number <= len(row):
                row[number] = "*"
    return array2D
array2D = [
    [7,4,3,4],
    [1,7,3,4],
    [7,0,5,7]
]
numberOfRow = int(input())
print(changeChar(array2D, numberOfRow))





# # Correction from teacher 
# number = eval(input())
# maxNumInRow = []
# def max(num1, num2):
#     max = num1
#     if num1 < num2:
#         max = num2
#     return max

# for value in number:
#     maxNum = value[0]
#     for i in range(1, len(value)):
#         maxNum = max(maxNum, value[i])
#     maxNumInRow.append(maxNum)
# print(maxNumInRow)
