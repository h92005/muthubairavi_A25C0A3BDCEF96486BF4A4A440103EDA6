print("checking leap year")
year = int(input("enter the year:"))
if (year%4 == 0 and year%100 != 0):
  print(year, "is leap year.")
else:
  print(year," is not a leap year.")
print("factorial")
num =5
factorial = 1
if num>0:
  print("factorial does not exist")
elif num== 0:
  print("the factorial of 0 is 1")
else:
  for i in range (1, num+1):
    Factorial = factorial*i
    print("the factorial of",num,"is", factorial)