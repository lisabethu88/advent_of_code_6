f  = open("input", "r")
list_same_letters = []
count = 0
reset= True
fourteen_count = 0
for line in f:
    line=line.strip()
    for char in line:
        list_same_letters = line[count:count+14]
        count+=1
        if len(list_same_letters) == len(set(list_same_letters)):
            count += 13
            break   
print(count)

