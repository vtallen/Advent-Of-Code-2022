from heapq import nlargest

elves_inventory_file = open("elves_inventory.txt", "r")

#The current elf we are adding up the total for
elf_number = 0

#This is flipped to True if we have reached a new line and need to create a new elf in the elves dictionary
start_of_inventory = False

#The current total of the elf we are adding up
current_total = 0

#The contents of all the elves' inventories
food_items = elves_inventory_file.readlines()

#The total number of calories in  each elf's inventory
elves = {
    "Elf_0": 0
}

for food_item in food_items:
    #If we get to a new line, begin adding up another elf's inventory
    if food_item == "\n":
        elf_number += 1
        start_of_inventory = True
        continue
    else:
        elf_name = "Elf_" + str(elf_number)
        food_item.strip("\n")

        if start_of_inventory == True:
            elves[elf_name] = 0
            start_of_inventory = False

        #Get the current total for the elf we are working on, then add the current item to it
        current_total = elves[elf_name]
        current_total += int(food_item)

        #Set the current elf's inventory to the current_total
        elves[elf_name] = current_total

#Using nlargest to get the 3 elves with the most calories in their inventory
top_3_elves = nlargest(3, elves, key=elves.get)
top_3_elves_total = 0

elf_number = 0
print("Elves with the most calories in their inventories:\n")
for elf in top_3_elves:
    num_calories = elves[elf]

    print(top_3_elves[elf_number] + " : " + str(num_calories))
    top_3_elves_total += num_calories
    elf_number += 1

print("Total:", str(top_3_elves_total))