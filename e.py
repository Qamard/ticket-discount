group1 = int(input("Age of group1 : "))
group2 = int(input("Age of group2 : "))
group3 = int(input("Age of group3 : "))
group4 = int(input("Age of group4 : "))
group5 = int(input("Age of group5 : "))

group = [group1, group2, group3, group4, group5]

discount = min(group)

ticketPrice = 10
lenGroup = len(group)
ticketTotal = ticketPrice * lenGroup

total = ticketTotal - (ticketTotal * discount / 100)
print("The total Price is : " + str(total))