#discount calc
bill_amt = float(input("Enter bill amount:"))
if bill_amt > 1000 and bill_amt <= 1500:
    discount = 0.1 * bill_amt
    newbill_amt = bill_amt - discount
elif bill_amt > 1500 and bill_amt <= 2000:
    discount = 0.15 * bill_amt
    newbill_amt = bill_amt - discount
elif bill_amt > 200 and bill_amt <= 5000:
    discount = 0.2 * bill_amt
    newbill_amt = bill_amt - discount
elif bill_amt > 5000:
    discount = 0.25 * bill_amt
    newbill_amt = bill_amt - discount
print("The Initial Bill was:",bill_amt)
