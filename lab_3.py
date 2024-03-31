age=int(input("Enter Your Age: "))
if age<=12:
         print("You are eligible for discount on the movie ticket")
elif age >=13 and age<=18:
          student =input("Are you student:")
          if student=='yes' or student== 'Yes' or student == 'Y' or student == 'y':
                    print("You are eligible for discount on the movie ticket")
          else:
                    print("You are not eligible for the discount on the movie ticket")
else:
          print(" You are not eligible for the discount on the movie ticket:!")