# # # 1
# def updateNum(arr):
#     for i in range(len(arr)):
#         if arr[i]<10:
#             arr.pop(i)
#             arr.insert(i, 10)
#     return arr
# print(updateNum(eval(input())))

# # 3
# def transferNum(arr):
#     newNum = []
#     for i in range(len(arr)):
#         newNum.append(arr[i]+1)
#     return newNum
# print(transferNum(eval(input())))

# #4
# def findIndexOfSeven(array):
#     index = []
#     for i in range(len(array)):
#         if array[i]!=7:
#             index.append(array[i])
#     return index

# array = eval(input())
# print(findIndexOfSeven(array))

# # 5
# def replaceZero(array):
#     #write your code here:
#     newarr = []
#     for i in range(len(array)):
#         if array[i] == 1:
#             newarr.insert(i,0)
#         else:
#             newarr.append(array[i])
#     return newarr
# print(replaceZero(eval(input())))