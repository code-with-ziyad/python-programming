str1 = "Ziyad"
str2 = "Ahmed"

# length 
len = len(str1)
print(len)
# index number 
print(str1[3]) 

print(str1 +" " + str2)

# slice

str = "Ziyad Aftab"
print(str[2 :8]) # index 8 is not including all the character after 1 to before 8
print(str[2 :]) # 2 se lekr end index tak 
print(str[-5 : -1]) # python me nagative index bi hothe hai

# String function 1

string = "I am studying python from youtube"
print(string.endswith("youtube"))

# capitalize 

new = "my name is Ziyad"

new = new.capitalize()

print(new.capitalize())
print(new)

# replace

my = "i am still learning python"

print(my.replace("python", "java"))

# find

search = "i am study in AI ML "

print(search.find("L"))

# count

search = "i am study in AI ML "

print(search.count("am"))
