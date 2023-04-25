
# Use add_3
import adder  # adder is the script file containing add_3 func
import desc_list

a = int(float(input('a :')))
b = int(float(input('b :')))
c = int(float(input('c :')))

d = adder.add_3(a, b, c)
e = adder.triple(d)

print(f'd = {d}')
print(f'e = {e}')
