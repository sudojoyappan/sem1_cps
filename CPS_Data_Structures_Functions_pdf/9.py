entries = [
 {'name': 'Alice', 'score': 85},
 {'name': 'Bob', 'score': 90},
 {'name': 'Alice', 'score': 92},
 {'name': 'Charlie', 'score': 78},
 {'name': 'Bob', 'score': 88},
 {'name': 'Alice', 'score': 81}
 ]

def build_gradebook(entries):
    l=[]

    for i in entries:
        l.append(i['name'])
    s=set(l)
    d={}

    for j in l:
        l_new=[]

        for k in entries:
            if k['name']==j:
                l_new.append(k['score'])
                
        d[k['name']]=l_new
        l_new=[]

    return d

print(build_gradebook(entries))