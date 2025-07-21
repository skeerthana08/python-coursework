seats = {
    "U1":{'price':1029, 'booking_status':True}
    "U2":{'price':1029, 'booking_status':False}
    "U3":{'price':1029, 'booking_status':True}
    "U4":{'price':1029, 'booking_status':False}
    "U5":{'price':1029, 'booking_status':True}
    "U6":{'price':1029, 'booking_status':False}
    "L1":{'price':2029, 'booking_status':True}
    "L2":{'price':2029, 'booking_status':True}
    "L3":{'price':2029, 'booking_status':True}
    "L4":{'price':2029, 'booking_status':False}
    "L5":{'price':2029, 'booking_status':True}
}

for i in seats:
    if seats[i]['booking_status']:
        print(f'***{i}')
    else:
        print(f'{i}-{seats[i]["price"]}')
seatno=input("Enter the seat no: ").upper()
if seatno in seats:
    if seats[seatno]['booking_status']:
        print(f'{seatno} is already booked. Go for other one!!')
    else:
        name=input("Enter the name: ").title()
        age=int(input("Enter the age: "))
        gender=input("Enter your Gender(F or M): ").upper()
        if age<=5:
            print(f"Hello {name} your seat booked successfully with free of cost")
        elif age<15:
            print(f"Hello {name} yor seat booked successfully with the discount of 50% off \nTotal price={seats[section]['price']}")
        else:
            print(f"hello {name} your seat is booked successfully. Pay the amount 2029")
else:
    print("Enter the seat no properly")
        