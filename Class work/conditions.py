hr,mins=list(map(int,input("Enter the HH:MM :").split(":")))
if hr>=0 and hr<=24 and mins>=0 and mins<=59:
    if hr>=0 and hr<4:
        print("its high time, sleep!!!")
    elif hr>=4 and hr<12:
        print("gm")
    elif hr>=12 and hr<16:
        print("ga")
    elif hr>=16 and hr<21:
        print("ge")
    elif hr>=21 and hr<24:
        print("gn")
    
else:
    print("invalid input")

    
