#Algorithm for calculating total grocery bill by adding multiple items
total=0
item_price=int(input("Enter price of item:"))
while item_price!=0:
    total+=item_price
    item_price=int(input("Enter price of item:"))
print(total) 