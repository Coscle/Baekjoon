word = input().upper()
alphabet = list(set(word))

counts = []
for i in range(len(alphabet)):
    count = word.count(alphabet[i])
    counts.append(count)

if counts.count(max(counts)) > 1:
    print("?")

else:
    max_index = counts.index(max(counts))
    print(alphabet[max_index])

