# #1
# def contians(word, char1):
#     findChar = 0
#     for i in range(len(word)):
#         if word[i] == char1.upper:
#            findChar = 1
#     return findChar
# arr = input()
# firstLetter = input()
# secondLetter = input()
# result = 'NOT VALID'
# a = contians(arr, firstLetter)
# b = contians(arr, secondLetter)
# if a == b:
#     result = 'VALID'
# print(result)


# 2
# def reverse(text):
#     result = ''
#     for i in range(-1,-(len(text)+1),-1):
#         result += text[i]
#     return result
# word = input()
# print(reverse(word))

# # #3
# def multiplyWithinRange(startNumber, endNumber):
#     result = 1
#     for i in range(startNumber,endNumber+1):
#         result *= i
#     if startNumber>endNumber:
#         result = 0
#     return result
# startNum = int(input())
# endNum = int(input())
# print(multiplyWithinRange(startNum, endNum))


# #4
# def CountChar(word, char):
#     result = 0
#     for j in range(len(word)):
#         if word[j]==char:
#             result += 1
#     return result
# words = input()
# character = input()
# print(CountChar(words, character))



# 5
# def average(scores):
#     sum = 0
#     perStudent = 0
#     for i in range(scores):
#         findAver = eval(input())
#         for i in findAver:
#             sum += i/len(findAver)
#     return sum/scores
# number = int(input())
# print(average(number))



