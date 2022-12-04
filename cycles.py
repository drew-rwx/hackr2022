
# Example graph
graph = {
	"A": ["B"],
	"B": ["C", "E"],
	"C": ["F"],
	"D": ["A"],
	"E": ["H", "D"],
	"F": ["I", "E"],
	"G": ["D"],
	"H": ["G"],
	"I": ["H"],
}

# graph = {
# 	"A": ["B", "D"],
# 	"B": ["C"],
# 	"C": ["F"],
# 	"D": ["E", "G"],
# 	"E": ["B", "F", "H"],
# 	"F": [],
# 	"G": ["H"],
# 	"H": ["I"],
# 	"I": ["F"],
# }

# graph = {
# 	"A": ["B", "D"],
# 	"B": ["C"],
# 	"C": ["F"],
# 	"D": ["E", "G"],
# 	"E": ["B", "H"],
# 	"F": ["E"],
# 	"G": ["H"],
# 	"H": ["I"],
# 	"I": ["F"],
# }

all_cycles = [
]

for starting_node in graph:

	# Add initial paths from the starting_node
	cycles = []
	for dest in graph[starting_node]:
		cycles.append([dest])

	walking = True

	# While our cycles aren't finished
	while walking:

		completed_cycles = 0

		# For each cycle
		for c in range(len(cycles)):

			# If we removed cycles without adding any back, c can be larger
			if c >= len(cycles):
				break

			# Break if cycle is complete
			if starting_node in cycles[c]:
				completed_cycles += 1
				continue

			# Grab last node
			last_node = cycles[c][-1]

			# Case 1: Out degree > 1
			if len(graph[last_node]) > 1:
				p = cycles.pop(c) # Remove old cycle

				# Add new cycles
				for dest in graph[last_node]:
					# Don't add if we revist a node
					if dest in p:
						continue
					new_cycle = p.copy()
					new_cycle.append(dest)
					cycles.append(new_cycle)

			# Case 2: Out degree == 1
			elif len(graph[last_node]) == 1:
				if graph[last_node][0] not in cycles[c]:
					cycles[c].append(graph[last_node][0])
				else:
					cycles.pop(c)

			# Case 3: Out degree == 0
			else:
				cycles.pop(c) # Remove because we hit a deadend

		# If all paths lead back to the starting node, we can stop walking the graph
		if completed_cycles == len(cycles):
			walking = False
		else:
			completed_cycles = 0

	# Add cycles to all cycles list
	all_cycles += cycles

# Remove repeats
for c in range(len(all_cycles)):
	min_val = min(all_cycles[c])
	min_val_index = all_cycles[c].index(min_val)

	for _ in range(len(all_cycles[c]) - min_val_index):
		all_cycles[c].insert(0, all_cycles[c].pop())

temp = []

for c in all_cycles:
	if c not in temp:
		temp.append(c)

all_cycles = temp

# Print results
for c in all_cycles:
	print(c)
