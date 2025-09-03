text = input("Enter a string: ")

total_chars = len(text)
unwanted_count = 0
for ch in text:
    if ch == ' ' or ch == '.' or ch == ',' or ch == '!':
        unwanted_count += 1

result = total_chars - unwanted_count

print(result)