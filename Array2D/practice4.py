
# 1
def hasMonsterOnCell (monsterPosition, cellX, cellY):
    result = False
    for i in range(len(monsterPosition)):
        if monsterPosition[i][0] == cellX and monsterPosition[i][1] == cellY:
            result = True
    return result
    # Write your code here !
    
# MAIN CODE 
values = eval(input())
for i in range(5):
    a = ""
    for j in range(5):
        if hasMonsterOnCell(values,j,i):
            a += "*"
        else:
            a += "0"  
    print(a)


# 2
array2D = [
    [3,9,1],
    [2,3,4],
    [2,5,1]
]
result = []
for row in array2D:
    odd = 0
    for col in row:
        if col % 2 == 1:
            odd += 1
    result.append(odd)
print(result)

# 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
array2D = eval(input())
result = []
for row in range(len(array2D[0])):
    sum = 0
    average = 0
    for col in range(len(array2D)):
        sum += array2D[col][row]
        average += 1
    sum = sum // average
    result.append(sum) 
        
print(result)