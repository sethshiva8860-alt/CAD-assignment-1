def even_numbers(t):
    even_no = ()
    for num in t:
        if num % 2 == 0:
            even_no += (num,)
    return even_no

numbers = (1, 2, 3, 4, 5, 6, 7, 8)# Example tuple
result = even_numbers(numbers)# Function call

print("Even numbers tuple:", result)