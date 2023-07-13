import numpy as np

grid = [
        [0, 1, 1],
        [0, 0, 0],
        [0, 2, 0],
        [0, 0, 0]
    ]

step_cost = 0.04

# Probability of going in the direction of the action
p_action = 0.7
# Probability of going in a direction perpendicular to the action
p_perpendicular = 0.15
gamma = 0.95


U = [
        [0, 1, -1],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


n = 4
m = 3


def check(i, j):
    return i >= 0 and i < n and j >= 0 and j < m and grid[i][j] != 2


def calc_iter(U, grid):
    Unext = [
        [0, 1, -1],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i in range(n):
        for j in range(m):
            # print(U[i][j])
            if (grid[i][j] == 2 or grid[i][j] == 1):
                continue
            v = [-np.inf,-np.inf,-np.inf,-np.inf]
            sum = 0
            if check(i-1, j):
                sum = (p_action*U[i-1][j])
            else:
                sum = (p_action*U[i][j])
            if check(i,j-1):
                sum += (p_perpendicular*U[i][j-1])
            else:
                sum += (p_perpendicular*U[i][j])
            if check(i,j+1):
                sum += (p_perpendicular*U[i][j+1])
            else:
                sum += (p_perpendicular*U[i][j])
            v[0] = -step_cost + gamma*sum



            if check(i+1, j):
                sum = (p_action*U[i+1][j])
            else:
                sum = (p_action*U[i][j])
            if check(i,j-1):
                sum += (p_perpendicular*U[i][j-1])
            else:
                sum += (p_perpendicular*U[i][j])
            if check(i,j+1):
                sum += (p_perpendicular*U[i][j+1])
            else:
                sum += (p_perpendicular*U[i][j])
            v[1] = -step_cost + gamma*sum





            if check(i, j-1):
                sum = (p_action*U[i][j-1])
            else:
                sum = (p_action*U[i][j])
            if check(i-1,j):
                sum += (p_perpendicular*U[i-1][j])
            else:
                sum += (p_perpendicular*U[i][j])
            if check(i+1,j):
                sum += (p_perpendicular*U[i+1][j])
            else:
                sum += (p_perpendicular*U[i][j])
            v[2] = -step_cost + gamma*sum



            if check(i, j+1):
                sum = (p_action*U[i][j+1])
            else:
                sum = (p_action*U[i][j])
            if check(i-1,j):
                sum += (p_perpendicular*U[i-1][j])
            else:
                sum += (p_perpendicular*U[i][j])
            if check(i+1,j):
                sum += (p_perpendicular*U[i+1][j])
            else:
                sum += (p_perpendicular*U[i][j])
            v[3] = -step_cost + gamma*sum
                
            Unext[i][j] = max(v[0],v[1],v[2],v[3])
            # print(np.max(v),end='\t\t')
        # print()
    # print(Unext)
    for i in range(n):
        for j in range(m):
            if abs(Unext[i][j]-U[i][j]) > 0.0001:
                return Unext,1
    return Unext,0

flag = 1
cnt = 0
while flag:
    U, flag = calc_iter(U,grid)
    # print(U)
    cnt = cnt + 1
    print("Iteration:",cnt)
    for i in range(n):
        for j in range(m):
            print(U[i][j],end='\t')
        print()
    print('\n\n')
print("Total Number of Iterations:",cnt)




# bonus - calculate policy of each cell

dir = ['up','down','left','right']

print("\n#Policy for each cell after the algorithm converges\n")
for i in range(n):
    for j in range(m):
        # print(grid[i][j])
        if (grid[i][j] == 2):
            print('wall,\t\t',end='')
            continue    
        if (grid[i][j] == 1):
            print('absorb,\t\t',end='')
            continue

        v = [-np.inf,-np.inf,-np.inf,-np.inf]
        sum = 0
        if check(i-1, j):
            sum = (p_action*U[i-1][j])
        else:
            sum = (p_action*U[i][j])
        if check(i,j-1):
            sum += (p_perpendicular*U[i][j-1])
        else:
            sum += (p_perpendicular*U[i][j])
        if check(i,j+1):
            sum += (p_perpendicular*U[i][j+1])
        else:
            sum += (p_perpendicular*U[i][j])
        v[0] = -step_cost + gamma*sum



        if check(i+1, j):
            sum = (p_action*U[i+1][j])
        else:
            sum = (p_action*U[i][j])
        if check(i,j-1):
            sum += (p_perpendicular*U[i][j-1])
        else:
            sum += (p_perpendicular*U[i][j])
        if check(i,j+1):
            sum += (p_perpendicular*U[i][j+1])
        else:
            sum += (p_perpendicular*U[i][j])
        v[1] = -step_cost + gamma*sum





        if check(i, j-1):
            sum = (p_action*U[i][j-1])
        else:
            sum = (p_action*U[i][j])
        if check(i-1,j):
            sum += (p_perpendicular*U[i-1][j])
        else:
            sum += (p_perpendicular*U[i][j])
        if check(i+1,j):
            sum += (p_perpendicular*U[i+1][j])
        else:
            sum += (p_perpendicular*U[i][j])
        v[2] = -step_cost + gamma*sum



        if check(i, j+1):
            sum = (p_action*U[i][j+1])
        else:
            sum = (p_action*U[i][j])
        if check(i-1,j):
            sum += (p_perpendicular*U[i-1][j])
        else:
            sum += (p_perpendicular*U[i][j])
        if check(i+1,j):
            sum += (p_perpendicular*U[i+1][j])
        else:
            sum += (p_perpendicular*U[i][j])
        v[3] = -step_cost + gamma*sum

        ind = 0
        temp_list = []
        for k in range(4):
            if v[ind]<v[k]:
                ind = k

        for k in range(4):
            if v[ind]==v[k]:
                temp_list.append(dir[k])
        for dir_val in temp_list:
            print(dir_val,end=',')
        print(end='\t\t')
    print()
            