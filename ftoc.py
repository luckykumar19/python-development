def temp_convert():
    while True:
        print("Enter 1 to convert from celsius to fahrenheit")
        print("Enter 2 to convert from fahrenheit to celsius")
        print("Enter 0 to exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
         c=float(input("Enter temperature in celsius"))
         f=(c*9/5)+32
         print("Temperature in Fahrenheit is:",f)
        elif choice == 2:
           f=float(input("Enter temperature in fahrenheit"))
           c=(f-32)*5/9
           print("Temperature in Celsius is:",c)
        elif choice == 0:
           print("Exiting the program.")
           break
        else:
           print("Invalid choice")
    
           
temp_convert()
