files = [
 "script.py",
 "notes.txt",
 "data.csv",
 "main.py",
 "image.png",
 "list.txt"
 ]

def group_by_extension(f):
    l=[]
    d={}
    for file in f:
        file=file.split(".")
        l.append(file[1])
    s=set(l)
    for k in s:
        l_new=[]
        for l_ in f:
            if k in l_:
                l_new.append(l_)
        d[k]=l_new
    return d

print(group_by_extension(files))
