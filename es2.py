with open('input.txt') as f:
    lines = f.readlines()
mins = []
maxs = []
letters = []
passwords = []
data1 = []
data2 = []
for i in range(len(lines)):
    tmp = lines[i].split(" ")
    minmax = tmp[0].split("-")
    mins.append(int(minmax[0]))
    maxs.append(int(minmax[1]))
    letters.append(tmp[1].split(":")[0])
    passwords.append(tmp[2].split("\n")[0])

# Es 1
for i in range(len(lines)):
    tmp = 0
    for j in passwords[i]:
        if j == letters[i]:
            tmp += 1
    if tmp >= mins[i] and tmp <= maxs[i]:
        data1.append(passwords[i])

print(len(data1))

# Es 2
for i in range(len(lines)):
    tmp = 0
    if passwords[i][mins[i]-1] == letters[i]:
        tmp += 1
    if passwords[i][maxs[i]-1] == letters[i]:
        tmp += 1
    if tmp == 1:
        data2.append(passwords[i])

print(len(data2))

exit()