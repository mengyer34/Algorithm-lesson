# # 1
# word = input('Word : ')
# rule1 = 0
# rule2 = 0
# rule3 = 0
# for i in range(len(word)):
#     if word[i]=='A':
#         rule1 +=1
#     elif word[i] == 'B':
#         rule2 += 1
#     elif word[i] == 'C':
#         rule3 += 1
# message = 0
# if rule1 == 4:
#     message = '40'
# elif rule1 == 2 and rule2 == 2:
#     message = '20'
# elif rule3>0:
#     message = '10'
# print(message)

# # 2
# def sumIndexOfX(word):
#     result = 0
#     for i in range(len(word)):
#         char = word[i]
#         if char == 'X':
#             result += i
#     return result
# print(sumIndexOfX(input()))

#3
word = input()
findX = 0
countX = 0
findY = 0
for i in range(len(word)):
    char = word[i]
    if char == 'X':
        findX = i
        countX +=1
    elif char == 'Y':
        findY = i
message = 'NOT GOOD'
if findX < findY and countX > 0:
    message = 'GOOD'
print(message)








# # Khy Phat3:09 PM
# def findXBeforY(word):
#     xBeforY = False
#     yBeforX = False
#     for i in range(len(word)):
#         if word[i] == "X" and not xBeforY and not yBeforX:
#             xBeforY = True
#         elif word[i] == "Y" and not yBeforX:
#             yBeforX = True
#     xAndY = xBeforY and yBeforX
#     return xAndY
# word = input()    
# result = "NOT GOOD"
# if findXBeforY(word):
#     result = "GOOD"
# print(result)

