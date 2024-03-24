print("\nNewton's Second law of Motion")
print("..............................")
print("Enter the missing value: ")
print("1. Mass\n2. Acceleration\n3. force(F)")
missing_Value_choice=input("Enter the option number for the missing value:\n")
if missing_Value_choice == "1":
          a = float(input("Enter the acceleration Value:"))
          F = float(input("Enter force:"))
          m = F/a
          print(f"Mass(m) = {m} kg")
elif missing_Value_choice =="2":
          m = float(input("Enter Mass:"))
          F = float(input("Enter force:"))
          a = F/m
          print(f"Acceleration = {a} m/s^2")
elif missing_Value_choice =="3":
          m = float(input("Enter mass:"))
          a = float(input("Enter Acceleration(a):"))
          f =m*a
          print(f"Force(F) ={f} Newton")
else:
          print("Invalid Choice:")
          