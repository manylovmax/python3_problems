# (ahabcjahbdcjbjj)  as   (a3b3c2dh2j4)

input_str = 'ahabcjahbdcjbjj'
letters = dict()

for c in input_str:
    letters[c] = letters.get(c, 0) + 1

print(letters.items())
result_str = ''
sorted_letters = sorted(list(letters.items()))
for k, v in sorted_letters:
    result_str += k+str(v)

print(result_str)
