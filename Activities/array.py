# my_array = ['i','y','g','n','e','M']
# for i in range(len(my_array)-1,-1,-1):
#     print(my_array[i])


#loop for string
# my_list = ['meng#yi','#', 'S#M']
# a = ''
# find = True
# for i in range(len(my_list)):
#     if my_list[i]!='#':
#         a += my_list[i]
#     else:
#         a += "------------------"
#         find = False
# print(a)


# #Loop for value
# my_list = ['meng#yi','#', 'S#M']
# for value in my_list:
#     print(my_list, str(value))




#Practice
# #1
# def numberOfsevens(array):
#     result = 0
#     for 


# #2
# def countNum(arr):
#     count = 0
#     for i in range(1,len(arr)):
#         if arr[i-1] < arr[i]:
#             count += 1
#     return count
# print(countNum(eval(input())))

# # Enter your code here.
# def findItemInArray(arr,index):
#     result = ''
#     for i in range(len(arr)):
#         if index==arr[i]:
#             result += arr[i]
#         # if index == arr[-1]:
#         #     result += arr[]
#     return result 
# array = eval(str(input())()
# index = int(input())
# print(findItemInArray(array,index))


# # # Array part 2
# def findOdd(arr):
#     isOdd = False
#     if arr % 2==1:
#         isOdd = True
#     return isOdd

# ne


# oddnumber = []
# for i in range(5):
#     number = eval(input())
#     for i in number:
#       if i%2!=0:
#         oddnumber.append(i)
# print(oddnumber)

# a = eval(input())
# a.insert(1,90)
# print(a)


# tip1
numbers = [6,3,4,3,2,5,3,5]
for i in numbers:
    if i%2 != 0:
        numbers.insert(i,3)
print(numbers)

# tip2
numbers = [6,3,4,3,2,5,3,5]
for i in numbers:
    numbers.insert(i%2==1,3)
print(numbers)


# # remove number3
# numbers = [6,3,4,3,2,5,3,5]
# i = 0
# for j in numbers:
#     if j== 3:
#         numbers.pop(i)
#     i +=1
# print(numbers)