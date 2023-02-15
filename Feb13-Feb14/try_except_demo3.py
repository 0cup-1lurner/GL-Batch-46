try:
    result = 12/0
except ZeroDivisionError:
    print("Please use a non-zero num as a divisor")
else:
    # If there is no exception this block is executed
    print("Block 3")
finally:
    # This block is executed irrepective of previous blocks
    print("Always executed")
    
# result = 12/0
print("2nd line")
