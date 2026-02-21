age = int(input("input your age: "))

if(age >= 18 and age <= 25):
   print("you can apply for police")
elif(age < 18):
   print("you are not eligible for this post! under age")
elif(age > 25):
   print("Your age is cross the age  limit!")
