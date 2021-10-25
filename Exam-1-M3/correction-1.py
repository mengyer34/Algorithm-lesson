# # 1
# def contains(word, char):
#     isFound = False
#     for value in word:
#         if value.upper() == char.upper():
#             isFound = True
#     return isFound

# word = input()
# char1 = input()
# char2 = input()
# message = "NOT VALID"
# if contains(word, char1) and contains(word, char2):
#     message = "NOT VALID"
# print(message)



# # 5
# def number(arr):
#     result = 0
#     number = int(input())
#     for i in range(number):
#         array = eval(input())
#         for i in arr:
#             result += i
#         result = result/len(arr)
#     return result


# # 5
# def average(arr):
#     result = 0
#     for i in arr:
#         result += i
#     result/=len(arr)
#     return result
# def sum(array):
#     result1 = 0
#     for i in range(array):
#         arr = eval(input())
#         result1 += average(arr)
#     result1 /= array
#     return result1
# number = int(input())
# print(sum(number))


# def findaverage(number2):
#     sum = 0
#     for i in range(len(number2)):
#         sum += number2[i]
#     average = sum/len(number2)
#     return average
# def allaverage (number1):
#     sumvalue = 0
#     totalaverage = 0
#     for n in range(number1):
#         number3 = eval(input("score of student :"))
#         average = findaverage(number3)
#         sumvalue += average
#     totalaverage = sumvalue/number1
#     return totalaverage
# number = int(input("number of sutdent :"))
# print(allaverage(number))
