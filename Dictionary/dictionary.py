# a = { key: value, key: value}
# a = {"cambodia": 1, "thailand": 2, "me": 3}
# print(a)

# Add item 
studentsName = {}
studentsName['Tim'] = 23
studentsName['Rath'] = 20
studentsName['Rat'] = 21
print(studentsName)


# Loop
for key in studentsName:
    # for key 
    print(key)
    # for value
    print(studentsName[key])

# Remove items
studentsName.pop('Rat')
print(studentsName)