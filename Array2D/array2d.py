# # Ex 
# number =[
#     #column  0 1 2   row
#             [1,2,3], # 0
#             [4,5,6], # 1
#             [7,8,9]  # 2
# ]

# # print(number[row][column])
# print(number[2][2])


# # Practice 
# # # Ex1 
# a = [[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# result = ""
# for i in a[0]:
#     result += str(i) + "-"
# print(result)

# # # Ex2 
# a = [[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# result = ""
# for i in a[2]:
#     result += str(i) + "-"
# print(result)


# # Ex3 
# a = [[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# result = ""
# for i in range(len(a)):
#     result += str(a[i][3]) + "-"
# print(result)


# # Replace Number
# # You must to loop 2 time in array 2D
# number = [
#     [1,2,1],
#     [4,1,6],
#     [7,8,1]
# ]

# for i in range(len(number)):
#     arr = number[i]
#     for j in range(len(arr)):
#         if arr[j] == 1:
#             arr[j] = 0
# print(number)


# Append 
number = []
a = []
a.append(2)
b = []
b.append(4)
number.append(a)
number.append(b)
print(number)


