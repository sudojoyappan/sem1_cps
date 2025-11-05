s="hello world"
s1=""
vowel="aeiou"
v=0
nums="12345"
for i in range(len(s)):
    if s[i].lower() in vowel:
        v+=1
        s1+=nums[vowel.find(s[i])]
    else:
        s1+=s[i]
print(s1)
