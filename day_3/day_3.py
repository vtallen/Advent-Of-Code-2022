import string
import numpy as np

rucksack_contents_file = open("rucksack_contents.txt", "r")

rucksack_contents = rucksack_contents_file.readlines()

loopNum = 0
for group in rucksack_contents:
    rucksack_contents[loopNum] = rucksack_contents[loopNum].strip("\n")
    loopNum += 1

lowercase_priority_map = {}
uppercase_priority_map = {}

misplaced_items = []
sum_misplaced_items = 0

elf_groups = []

# Create the priority map for lowercase letters
lowercase_letters = string.ascii_lowercase
for i in range(1, 27):
    # This variable lets us get the correct letter from the lowercase_letters array
    letter_number = i - 1
    lowercase_priority_map[lowercase_letters[letter_number]] = i

'''
To create the uppercase letters priority map, we will iterate over a range of 26 to select each uppercase letter,
then we add 27 to i to get the correct priority value
'''
uppercase_letters = string.ascii_uppercase
for i in range(0, 26):
    letter_priority = i + 27
    uppercase_priority_map[uppercase_letters[i]] = letter_priority

for line in rucksack_contents:
    first_compartment = line[:len(line) // 2]
    second_compartment = line[len(line) // 2:]

    first_compartment = np.array(list(first_compartment))
    second_compartment = np.array(list(second_compartment))

    in_both = np.intersect1d(first_compartment, second_compartment)
    for item in in_both:
        misplaced_items.append(item)

for item in misplaced_items:
    if item.islower() == True:
        sum_misplaced_items += lowercase_priority_map.get(item)
    else:
        sum_misplaced_items += uppercase_priority_map.get(item)

print("All misplaced items: ", misplaced_items)
print("Sum of their priorities:", sum_misplaced_items)
print("\n")

def find_badge(arr1, arr2, arr3):
    # turn each rucksack's contents into a set
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)

    # find the common value between s1 and s2
    set1 = s1.intersection(s2)

    # find the common value between the common values of s1 and s2 with s3
    result_set = set1.intersection(s3)

    # Since you cannot directly access a value in a set, we have to iterate over the set and store the value in a variable
    badge_from_set = ""
    for i in result_set:
        badge_from_set = i

    return badge_from_set


loop_num = 0
group_num = 1

find_groups = True

badges = []
sum_badges = 0

while find_groups == True:
    elf_1 = list(rucksack_contents[loop_num])
    elf_2 = list(rucksack_contents[loop_num + 1])
    elf_3 = list(rucksack_contents[loop_num + 2])

    badge = find_badge(elf_1, elf_2, elf_3)
    print("Group: " + str(group_num) + " Badge: " + badge)

    badges.append(badge)

    loop_num += 3
    if (loop_num + 3) > len(rucksack_contents):
        find_groups = False

    group_num += 1

#Add up the badge priorities
for item in badges:
    if item.islower() == True:
        sum_badges += lowercase_priority_map.get(item)
    else:
        sum_badges += uppercase_priority_map.get(item)

print("\n")
print("Sum of group badge priorities:", sum_badges)