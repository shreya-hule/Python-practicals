def factorial(n):
	if n < 0:
		raise ValueError("n must be non-negative")
	if n == 0 or n == 1: # base case
		return 1
	return n * factorial(n - 1) # recursive case
def recursive_search(items, target, index=0):
	if index >= len(items): # base case: end reached
		return -1
	if items[index] == target:
		return index
	return recursive_search(items, target, index + 1)

print(factorial(5)) # 120
print(recursive_search([8, 3, 12, 7], 12)) # 2
print(recursive_search([8, 3, 12, 7], 5)) # -1