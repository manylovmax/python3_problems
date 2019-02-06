ALPHABET = dict()
n = input()

for x in input().lower():
        ALPHABET[ord(x) - ord('a')] = True

i = 0
for x in ALPHABET:
    if ALPHABET[x] == True: i += 1

if i != 26:
    print("NO")
else:
    print("YES")

# print(i)

# TheQuickBrownFoxJumpsOverTheLazyDog