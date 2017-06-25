s = 'azcbobobegghakl'
count = 0;

#We go through for each character in the string
for char in s:
    #When we find a valid character we increment the counter
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print(count)
