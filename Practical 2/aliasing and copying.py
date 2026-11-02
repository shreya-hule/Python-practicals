original = [1, 2]
alias = original
copy_list = original.copy()
alias.append(3)
print("original:", original)
print("alias:", alias)
print("copy:", copy_list)
# original: [1, 2, 3]\nalias: [1, 2, 3]\ncopy: [1, 2]