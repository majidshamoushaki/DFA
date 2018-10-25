states = dict()
file = open("secondNFA.txt", 'r')
line = file.read()
i = 0
while (i < len(line) - 1):
    first_node = line[i]
    i = i + 1
    edge = line[i]
    i = i + 1
    next_node = line[i]
    i = i + 1
    if first_node in states.keys():
        if edge in states[first_node].keys():
            states[first_node].get(edge).append(next_node)
        else:
            states[first_node].update({edge: [next_node]})
    else:
        states.update({first_node: {edge: [next_node]}})

print(states)

string = input("enter string: ")
start = input("enter start state: ")
final = input("enter final state: ")
curr_state = start
print(states)


def next_state(states, curr_state, i):
    if states[curr_state].get(string[i]):
        print(curr_state, end=" ")
        for j in range(0, len(states[curr_state].get(string[i]))):
            if states[curr_state].get(string[i])[j]:
                curr_state = states[curr_state].get(string[i])[j]
                if curr_state == final and i == len(string) - 1:
                    print(curr_state, end=" ")
                    print("Accepted")
                    exit(0)
                else:
                    if i + 1 != len(string):
                        next_state(states, curr_state, i + 1)


for i in range(0, len(states[start].get(string[0]))):
    next_state(states, curr_state, i)
print("Rejected!")
