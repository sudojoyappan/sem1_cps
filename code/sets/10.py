day1={}
day2={}
union=day1+day2
not_common=(day1-day2)+(day2-day1)
intersection=union-not_common
print(intersection)
print(not_common)
if day2.issuperset(day1):
    print(True)
