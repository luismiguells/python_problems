s = 'azcbobobegghakl'
count = 0;

#We go through but now to the len of the string
for i in range(len(s)):
    #We go 3 by 3 words until we find 'bob' that have 3 letters
    if s[i:i+3] == 'bob':
        count += 1
print(count)
