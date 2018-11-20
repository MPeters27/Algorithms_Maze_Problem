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
        initial_graph.update({arr[0] : [arr[1], arr[2]]})
    else:
        initial_graph.get(arr[0]).append(arr[1])
        initial_graph.get(arr[0]).append(arr[2])
