# # 1
# def isEqual(list1, list2):
#     isEqual = True
#     index = 0
#     for i in list1:
#         if i != list2[index]:
#             isEqual = False
#         index +=1
#     if isEqual:
#         message = "E"
#     else:
#         message = "N"
#     return message
# l1 = eval(input())
# l2 = eval(input())
# print(isEqual(l1,l2))

# # 2
# def countGreaterNum(arr):
#     result = 0
#     for i in range(1,len(arr)):
#         if arr[i-1] < arr[i]:
#             result += 1
#     return result
# print(countGreaterNum(eval(input())))
