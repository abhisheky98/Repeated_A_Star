from Grid_Generator import gen_grid
from Repeated_A_Star import repeated_a_star

def find_path(parent, dim):
    i,j = dim-1, dim-1
    path = [(dim-1,dim-1)]
    while (i,j) != (0,0):
        path.insert(0, parent[i][j])
        (i,j) = parent[i][j]
    return(path)

grid = gen_grid(5, 0.03)
grid = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 1], [0, 0, 0, 0, 0]]
#grid = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(grid)

for x in grid:
    print(x)

result, final, dis, cells, start, stop = repeated_a_star(grid, 5, 0.03, 2)

#path = find_path(parent, 5)

print("path")
print(final)

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
