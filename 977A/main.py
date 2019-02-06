args = [int(x) for x in input().split()]
a = list(str(args[0]))
b = int(args[1])

k = 0
while b > 0:
    k = int(a.pop())
    b -= k
    if b <= 0:
        a.append(str(-b))
        break
    else:
        b -= 1

a = ''.join(a)
print(a)
