with open('input.txt') as f:
    lines = f.readlines()
data=[]
for i in lines:
    data.append(int(i))

# Es 1
for i in data:
    for j in data:
        if i+j == 2020:
            print(i*j)
            exit()

# Es 2
for i in data:
    for j in data:
        for k in data:
            if i+j+k == 2020:
                print(i*j*k)
                exit()