word1 = "marco"
word2 = "brad"
# merged_string = ""
# remaining_string = ""
# shortest_index = None

# if len(word1) < len(word2):
#     shortest_index = len(word1)
#     remaining_string = word2[shortest_index:]
# else:
#     shortest_index = len(word2)
#     remaining_string = word1[shortest_index:]


# for i in range(shortest_index):
#     merged_string += word1[i]
#     merged_string += word2[i]

# merged_string += remaining_string

# print(merged_string)
i = 0

res = []

while i < len(word1) and i < len(word2):
    res.append(word1[i])
    res.append(word2[i])
    i += 1

res.append(word1[i:])
res.append(word2[i:])
return "".join(res)

