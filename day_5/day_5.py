import copy

stacks = {}
stacks_9001 = []


def create_stacks_dict(num_stacks):
    for n in range(1,(num_stacks+2)):
        stacks[n] = []


def append_stacks(input, first_run=True):
    #Gets each line of the stacks of crates and turns them into an array with each item containing a box
    line_stacks = []
    while input:
        line_stacks.append(input[:4])
        input = input[4:]
    if first_run:
        #If it is the first time the program has run, we need to initialize the stacks dictionary
        create_stacks_dict(len(line_stacks))

    #For every crate in every line of the puzzle input, append it to the appropriate stack in the stacks dictionary
    current_stack = 1
    for box in line_stacks:
        box = box.replace(" ", "").replace("\n", "").replace("[", "").replace("]", "")
        if box == "":
            current_stack += 1
        else:
            #Get the stack we are modifying, and append the new crate
            working_stack = stacks[current_stack]
            working_stack.append(box)

            #Replace the existing stack with the appended one
            stacks[current_stack] = working_stack
            current_stack += 1


def crate_mover_9000(num_crates, a, b):
    stack_a = stacks.get(int(a))
    stack_b = stacks.get(int(b))

    #Reverse the stacks so we can pop from the top of them
    stack_a.reverse()
    stack_b.reverse()

    #pop the number of crates from stack_a and append them to stack b
    for i in range(0, num_crates):
        stack_b.append(stack_a.pop())

    #Return the stacks to being top first
    stack_a.reverse()
    stack_b.reverse()

    #Store the modified stacks into the stacks dictionary
    stacks[int(a)] = stack_a
    stacks[int(b)] = stack_b

def crate_mover_9001(num_crates, a, b):
    stack_a = stacks_9001.get(int(a))
    stack_b = stacks_9001.get(int(b))


    #Reverse the stacks so we can pop from the top of them
    stack_a.reverse()
    stack_b.reverse()

    temp_stack = []
    #pop the number of crates from stack_a and append them to temp stack
    for i in range(0, num_crates):
        temp_stack.append(stack_a.pop())

    #Reverse temp_stack so that it will retain its order when we append it to stack_b
    temp_stack.reverse()

    for crate in temp_stack:
        stack_b.append(crate)

    #Return the stacks to being top first
    stack_a.reverse()
    stack_b.reverse()

    #Store the modified stacks into the stacks dictionary
    stacks_9001[int(a)] = stack_a
    stacks_9001[int(b)] = stack_b


puzzle_input_file = open("puzzle_input.txt", "r")
puzzle_input = puzzle_input_file.readlines()

#Takes in only the lines of the puzzle input with the stacks
num_lines_for_stacks = 0
stacks_input = []
for line in puzzle_input:
    if line == "\n":
        stacks_input.pop()
        num_lines_for_stacks += 1
        break
    stacks_input.append(line)
    num_lines_for_stacks += 1

#Adds the inital stacks to the stacks dictionary
create_stacks = True
for line in stacks_input:
    if create_stacks == True:
        append_stacks(line, first_run=True)
        create_stacks = False
    else:
        append_stacks(line, first_run=False)

#Creates a duplicate dictionary for the CrateMover9001
stacks_9001 = copy.deepcopy(stacks)

#Gets only the input after the stacks
box_moving_instructions = puzzle_input[num_lines_for_stacks:]

for instruction in box_moving_instructions:
    #Turn the instruction into a 3 number array
    instruction = instruction.replace("move", "").replace("from", "").replace("to", "").replace("\n", "").strip().split("  ")

    #Call the function to move the cratese with those three numbers
    crate_mover_9000(int(instruction[0]), instruction[1], instruction[2])
    crate_mover_9001(int(instruction[0]), instruction[1], instruction[2])


#Get the solution
part1_solution = []
part2_solution = []
for i in range(1,10):
    temp = stacks.get(i)
    part1_solution.append(temp[0])

for i in range(1, 10):
    temp = stacks_9001.get(i)
    part2_solution.append(temp[0])

print("Part 1 Solution:", part1_solution)
print("Part 2 Solution:", part2_solution)

