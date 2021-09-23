from Grid_Generator import gen_grid
from A_Star_test import a_star

def find_path(parent, dim):
    i,j = dim-1, dim-1
    path = [(dim-1,dim-1)]
    while (i,j) != (0,0):
        path.insert(0, parent[i][j])
        (i,j) = parent[i][j]
    return(path)

grid = gen_grid(10, 0.03)
#grid = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#print(grid)

for x in grid:
    print(x)

result, start, stop, parent, g, h, f, order = a_star(10, 0.5, grid, 2)

path = find_path(parent, 10)

print("order")
print(order)

print("path")
print(path)

print(result)
for x in parent:
    print(x)

print("g")
for x in g:
    print(x)

print("h")
for x in h:
    print(x)

print("f")
for x in f:
    print(x)
