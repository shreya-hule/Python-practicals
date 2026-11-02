numbers = [10, 20, 30]
numbers[0] = 99
numbers.append(40)
print(numbers) # [99, 20, 30, 40]
word = "python"
# word[0] = "P" # Uncomment: TypeError
word = "P" + word[1:]
print(word) # Python
point = (4, 5)
# point[0] = 9 # Uncomment: TypeError
print(point) # (4, 5)