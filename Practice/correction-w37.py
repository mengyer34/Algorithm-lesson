# 1
# word = eval(input())
# newWord = []
# for i in word:
#     for j in i:
#         if j not in newWord:
#             newWord.append(j)
#     newWord.sort()
# print(newWord)


# # 5
# word = eval(input())
# newWord = []
# for i in word:
#     for j in i:
#         if j not in newWord:
#             newWord.append(j)
# print(newWord)


# word = str(newWord)
# for i in range(len(word)):
#     result = ''
#     if word[i] != ',':
#         result.append(word[i])



# 3 Remove 7
def findIn7(array):
    index = 0
    for i in range(len(array)):
        if array[i]==7:
            index = i
    return index
array = eval(input())
array.pop(findIn7(array))
print(array)