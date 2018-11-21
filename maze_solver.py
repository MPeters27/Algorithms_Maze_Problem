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

# create the graph adjacency list
visited = []
state = (S1, S2)
visited.append(state)
paths = {}

for i in range(1, N):
    for j in range(1, N):
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
processed = []
stack = []
stack.append((S1, S2))
visited.append((S1, S2))
no_options = True
test = stack[0]

while N not in test:
    arr = paths.get(test)
    if arr is None:
        arr = []
    for i in range(len(arr)):
        if arr[i] in processed or arr[i] in visited:
            continue
        else:
            no_options = False
            stack.append(arr[i])
            visited.append(arr[i])
            test = arr[i]
            break
    if no_options is True:
        processed.append(stack[len(stack) - 1])
        stack.pop()
        visited.pop()
        test = stack[len(stack)-1]
    no_options = True

# captain rocket lieutenant lucky
# print the result

file2 = open("maze_output", "w")

for i in range(1, len(stack)):
    after = stack[i]
    before = stack[i-1]
    if after[0] != before[0]:
        file2.writelines("R " + str(after[0]) + "\n")
    else:
        file2.writelines("L " + str(after[1]) + "\n")



