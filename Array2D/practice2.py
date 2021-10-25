# #1
# array2D = [
#     ['a','b','c'],
#     ['k','b','d'],
#     ['a','bg','d']
# ]

# array = []
# for row in array2D:
#     element = ''
#     for col in range(len(row)):
#         element += row[col].lower()
#     array.append(element)
# print(array)


# #2
# array2D = [
#     [2,0,1],
#     [2,3,4],
#     [2,2,1]
# ]


# result = []
# for row in range(len(array2D)):
#     sum = 0
#     for col in range(len(array2D[row])):
#         sum += array2D[col][row]
#     result.append(sum)
# print(result)

# input_val = [[1, 2, 3, 4, 5],
#              [1, 2, 3, 4, 5],
#              [1, 2, 3, 4, 5]]

# vals_length = len(input_val[0])
# output_val = [0] * vals_length # init empty output array with 0's
# for i in range(vals_length): # iterate for each index in the inputs
#     for vals in input_val:
#         output_val[i] += vals[i] # add to the same index

# print(output_val) # [3, 6, 9, 12, 15]




# # 3
# array2D = [
#     [2,9,1],
#     [2,3,4],
#     [2,2,1]
# ]
# result = []
# for row in range(len(array2D[0])):
#     a = array2D[0][row]
#     for col in range(len(array2D)):
#         if a > array2D[col][row]:
#             a = array2D[col][row]
#     result.append(a)
# print(result)

# #4 
# persons = eval(input())
# age = int(input())
# result = ""
# for row in persons:
#     if row[2] == age:
#         result += row[0]+"\n"
# print(result)

# 
# 

# number = input()
# sum = 0
# index = 0
# max = 0
# min = 0
# while number != 'q':
#     index += 1
#     sum += int(number)
#     if max < int(number):
#         max = int(number)
#     else:
#         min = int(number)
#     number = input()
# average = sum/index

# print(average)
# print(max)
# print(min)