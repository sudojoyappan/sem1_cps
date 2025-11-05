dinner_guests={}
afterparty_guests={}
union=dinner_guests+afterparty_guests
print(union-((dinner_guests-afterparty_guests)+(afterparty_guests-dinner_guests)))
print(dinner_guests-afterparty_guests)
print(afterparty_guests-dinner_guests)
print(union)