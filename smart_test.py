from Smart_Repeated_A_Star import smart_repeated_a_star
from Grid_Generator import gen_grid

#grid = gen_grid(5, 0)
grid = [[0, 0, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(grid)
for x in grid:
    print(x)

result, final, dis, cells, start, stop = smart_repeated_a_star(grid, 5, 0.3, 2)

print(result)
print(final)
