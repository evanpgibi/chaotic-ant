def turnRight():
    global x, y, direction
    if L[y][x] == 0:
        L[y][x] = 1
    else:
        L[y][x] = 0

    if direction == "north":
        direction = "east"
        x += 1
    elif direction == "east":
        direction = "south"
        y += 1
    elif direction == "south":
        direction = "west"
        x -= 1
    elif direction == "west":
        direction = "north"
        y -= 1

def turnLeft():
    global x, y, direction
    if L[y][x] == 0:
        L[y][x] = 1
    else:
        L[y][x] = 0

    if direction == "north":
        direction = "west"
        x -= 1
    elif direction == "west":
        direction = "south"
        y += 1
    elif direction == "south":
        direction = "east"
        x += 1
    elif direction == "east":
        direction = "north"
        y -= 1

i=int(input("iterations:"))
L= matrix = [[0 for _ in range(66)] for _ in range(66)]

x=33
y=33
direction="north"

for j in range(i):
    if L[y][x] == 0:
        turnRight()
    else:
        turnLeft()
for i in L:
    print(i)