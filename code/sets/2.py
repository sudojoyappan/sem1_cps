words= ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
unique_words=[]
frequency={}
s=set(words)
for i in s:
    frequency[i]=0
for i in words:
    frequency[i]=words.count(i)
print(frequency)