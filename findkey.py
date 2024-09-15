total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else: 
            total -= i - j

counter = 0
while counter < 5:
    if total < 13: 
        total += 1
    elif total > 13: 
        total -= 1
    else:
        counter += 2 

# print(total)
# print(counter)

# Github link https://github.com/Shantanu-Barua/HIT137_asgn2.git 