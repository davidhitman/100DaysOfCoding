# print all instrunctions and prompt user to enter bill
print("Welcome to the bill calculator")
total_bill= input("What is the total bill?")
tip_entered = True
# check if the tip entered is with in the allowed range
while tip_entered:
    tip = int(input("What percentage tip would you like to give? 0, 10, 12, or 15?"))
    if (tip==0):
        tip_entered = False
    elif (tip==10):
        tip_entered = False
    elif (tip == 12):
        tip_entered = False
    elif (tip == 15):
        tip_entered = False
num_people_paying = input("how many people are splitting the bill?")
# calculate the total pay including the tip
total_pay = float(total_bill)+ ((tip/100)*float(total_bill))
# divide the total pay with all the individuals paying
# the {:.2f} specifies that the float should be in 2 decimal places
each_person = "{:.2f}".format(total_pay/float(num_people_paying))
# print your answer
print(f"Each Person should pay: £{each_person}")
