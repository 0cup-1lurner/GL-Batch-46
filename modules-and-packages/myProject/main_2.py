
# Use add_3
def add_3(x, y, z):
    return x + y + z
# Use triple
def triple(n):
    return n + n + n  # 3*n

a = int(float(input('a :')))
b = int(float(input('b :')))
c = int(float(input('c :')))

d = add_3(a, b, c)
e = triple(d)

print(f'd = {d}')
print(f'e = {e}')
