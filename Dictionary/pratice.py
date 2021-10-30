# # 1
# listStudent = {'2021A':20, '2021B': 30, '2021C':15}
# for key in listStudent:
#     print("Class", key, "has", listStudent[key],  "students")

# # 2 
# listStudent = {"2021A":20, "2021B":30, "2021C":15}
# value = int(input())
# key = input()
# listStudent[key] += value
# for i in listStudent:
#     print("Class", i, "has", listStudent[i],  "students")

# # 3
# listStudent_one = {'2021A':20, '2021B': 30, '2021C':15}
# listStudent_two = {'2021A':15, '2021C': 10, '2021D':99}
# # The way to merge 
# # newList = {**listStudent_one, **listStudent_two}
# newList = {}
# for key in listStudent_one:
#     for keys in listStudent_two:
#         if key == keys:
#             value = listStudent_one[key] + listStudent_two[key]
#             newList[key] = value
    
# print(newList)
        # else:
        #     print(key)
            # newList[key] += keys
        # else:
        #     newList += listStudent_two[keys]
# print(newList)