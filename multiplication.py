num = int(input("Enter the number to multiply: "))
num2 = int(input("Enter the limit: "))
print(f"\nMultiplication of {num}:[ 1 to {num2} ]")
for i in range(1,num2+1):
          print(f"{num} X {i} = {int(num)*i}")