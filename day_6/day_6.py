packet_file = open("packet.txt", "r")
packet = list(packet_file.readline())
packet_file.close()

id_array = []
char_processed = 0

def cycle_char():
    id_array.reverse()
    id_array.pop()
    id_array.reverse()


for ch in packet:
    id_array.append(ch)
    char_processed += 1
    id_set = set(id_array)

    if len(id_array) == 4:
        if len(id_set) == len(id_array):
            print("4 Unique characters found!")
            print("Datastram start:", id_array)
            print("Characters processed:", char_processed)
            print("")
            break
        else:
            cycle_char()

for ch in packet[char_processed:]:
    id_array.append(ch)
    char_processed += 1
    id_set = set(id_array)

    if len(id_array) == 14:
        if len(id_set) == len(id_array):
            print("14 Unique characters found!")
            print("Message start marker:", id_array)
            print("Characters processed:", char_processed)
            print("")
            break
        else:
            cycle_char()


