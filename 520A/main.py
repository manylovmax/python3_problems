import string

ALPHABET = list(string.ascii_lowercase)
n = input()

for x in set(input().lower()):
        ALPHABET.remove(x)

if len(ALPHABET):
    print("NO")
else:
    print("YES")

# print(ALPHABET)

# TheQuickBrownFoxJumpsOverTheLazyDog