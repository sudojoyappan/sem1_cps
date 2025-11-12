packets=[1001, 1002, 1003, 1002, 1004, 1005, 1001, 1003, 1002]
def find_duplicate_packets(l):
    d={}
    for i in packets:
        if l.count(i)>1:
            d[i]=l.count(i)
    return d



print(find_duplicate_packets(packets))



