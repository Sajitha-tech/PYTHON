words = ["apple", "banana", "cherry", "blueberry"]

max_length = 0
for word in words:
    length = 0
    for char in word:
        length += 1 
    if length > max_length:
        max_length = length
print("Length of the longest word:", max_length)