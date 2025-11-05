checked_out={}
reserved={}
x=input("Enter a book name:")
if (x not in checked_out) and (x not in reserved):
    print(x,'is currently unavailable.')
if (x in reserved) and (x not in checked_out):
    print(x,'is reserved but not checked out')
c=0
if checked_out.count(x)>0:
    print('Checked out by multiple members.')