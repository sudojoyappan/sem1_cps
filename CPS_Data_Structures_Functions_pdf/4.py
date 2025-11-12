resolutions = [
 (1920, 1080),
 (1280, 720),
 (2560, 1440)
 ]
factor = 0.5

def scale_resolutions(r,f):
    l=[]
    for i in r:
        l_t=[]
        for j in i:
            l_t.append(j*f)
        l.append(tuple(l_t))
    return l

print(scale_resolutions(resolutions,factor))