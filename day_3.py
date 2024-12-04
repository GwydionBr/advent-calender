data = []
total_counter = 0

with open ('data/day_3.txt') as f:
    lines = f.readlines()
    for line in lines:
         data.append(line)


# -----------------------------------------------------------------------------------------------
# Part One

# for line in data:
#     for i in range(0, len(line) - 4):
#         if line[i:i+4] == "mul(":
#             for j in range(i+4, i+12):
#                 if line[j] == ")":
#                     items = line[i+4:j].split(",")
#                     if len(items) == 2:
#                         if items[0].isdigit() and items[1].isdigit():
#                             total_counter += int(items[0]) * int(items[1])

#                 else:
#                     continue
#         else:
#             continue
      
# print(total_counter)

# -----------------------------------------------------------------------------------------------
# Part Two

do = True

for line in data:
    for i in range(0, len(line) - 4):
        if line[i:i+4] == "do()":
            do = True
        elif line[i:i+7] == "don't()":
            do = False
        if line[i:i+4] == "mul(" and do:
            for j in range(i+4, i+12):
                if line[j] == ")":
                    items = line[i+4:j].split(",")
                    if len(items) == 2:
                        if items[0].isdigit() and items[1].isdigit():
                            total_counter += int(items[0]) * int(items[1])

                else:
                    continue
        else:
            continue
      
print(total_counter)