import sys
sys.path.append('../advent_of_code')
from input_data import get_data

text = get_data(13, 2023)
patterns = text.split('\n\n')

rcols = []
rrows = []
Gs = []
for p in patterns:
    rows = p.split('\n')
    Gs.append([[rows[i][j] for j in range(len(rows[0]))] for i in range(len(rows))])

# return how many differences are between the arrays
def check(arr1, arr2, counter):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            counter += 1
    return counter
        

for p2 in [False, True]:
    ans = 0
    limit = 1 if p2 else 0
    for g in Gs:
        goodR = False
        goodC = False
        
        # check row symmetry
        for i in range(len(g)-1):
            if check(g[i], g[i+1], 0) < 2:
                left = i
                right = i+1
                counter = 0
                while 0 <= left and right < len(g):
                    counter = check(g[left], g[right], counter)
                    if counter > limit:
                        goodR = False
                        break                
                    left -= 1
                    right += 1
                else:
                    if counter == limit:
                        goodR = True
                        break
        if goodR:
            # print('R', (i+1, i+2))
            ans += 100*(i+1)
        
        # check column symmetry
        for c in range(len(g[0])-1):
            col1 = []
            col2 = []
            for r in range(len(g)):
                col1.append(g[r][c])
                col2.append(g[r][c+1])
            if check(col1, col2, 0) < 2:
                left = c
                right = c+1
                counter = 0
                while 0 <= left and right < len(g[0]):
                    lef = []
                    rig = []
                    for i in range(len(g)):
                        lef.append(g[i][left])
                        rig.append(g[i][right])
                    counter = check(lef, rig, counter)
                    if counter > limit:
                        goodC = False
                        break
                    left -= 1
                    right += 1
                else:
                    if counter == limit:
                        goodC = True
                        break
        if goodC:
            # print('C', (c+1, c+2))
            ans += (c+1)

    print(ans)