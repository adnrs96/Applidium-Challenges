import random
input_wall =  map(int,raw_input().split(','))
output_wall = []
for i, app in enumerate(input_wall):
    try:
        swapable = random.randint(i+1,len(input_wall)-1)
        output_wall.append(input_wall[swapable])
        input_wall[swapable] = input_wall[i]
    except:
        output_wall.append(input_wall[i])
appwall = ','.join(map(str,output_wall))
print(appwall)
