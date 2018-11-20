# read the first line
file = open("maze_input", "r")
N = int(file.readline(2))
file.readline(1)
M = int(file.readline(2))
file.readline()

# read the second line
line2 = file.readline()
vertex_colors = line2[0::2]

# read the third line
S1 = int(file.readline(1))
file.readline(1)
S2 = int(file.readline(1))
file.readline()

# read the remaining lines
initial_graph = {}  # contains the initial graph data
for i in range(M):
    line = file.readline()
    line = line.replace("\n", "")
    arr = line.split(" ")
    temp = initial_graph.get(arr[0])
    if temp is None:
        initial_graph.update({arr[0]: [arr[1], arr[2]]})
    else:
        initial_graph.get(arr[0]).append(arr[1])
        initial_graph.get(arr[0]).append(arr[2])


# problem solving section
visited = []
state = (S1, S2)
visited.append(state)
paths = {}

for i in range(1, N-1):
    for j in range(1, N-1):
        if i == j:
            continue
        else:
            temp_paths = []
            color_x = vertex_colors[i - 1]
            color_y = vertex_colors[j - 1]
            arr1 = initial_graph.get(str(i))
            arr2 = initial_graph.get(str(j))

            if color_y in arr1:
                index = arr1.index(color_y)
                temp_paths.append((int(arr1[index - 1]), j))
            if color_x in arr2:
                index = arr2.index(color_x)
                temp_paths.append((i, int(arr2[index - 1])))

            paths.update({(i, j): temp_paths})

# problem solving section
visited = []
stack = []
stack.append((S1, S2))
visited.append((S1, S2))
no_options = True
S1prev = 0
S2prev = 0
test = stack[0]

while N not in test:

    arr = paths.get((S1, S2))
    if arr is None:
        arr = []
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        else:
            no_options = False
            visited.append(arr[i])
            stack.append(arr[i])
            S1prev = S1
            S2prev = S2
            S1 = arr[i][0]
            S2 = arr[i][1]
            test = arr[i]
            break
    if no_options is True:
        stack.pop()
        S1 = S1prev
        S2 = S2prev
        test = (S1, S2)
    no_options = True




