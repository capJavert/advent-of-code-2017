h = 0

for num in range(106500, 123500, step=17):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        h += 1

print(1001-h)
