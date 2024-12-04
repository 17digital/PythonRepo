#print("Hello World")
#print("It's really good!")
age = 35
gpa = 6.2
is_student = True
first_name = "Brian"
last_Name = "Jenkins"
full_Name = first_name +" "+ last_Name
print(first_name)
print(type(first_name)) # outputs the type of variable
print("Hello You must be "+full_Name)
print(f"Hello {full_Name}") # f means format -- insert/print a variable
print(f"You are {age} years old")
print(f"Your gpa {gpa}")
print(type(gpa))
print("Your gpa is: "+str(gpa)+" smarty")
print(f"Are you a student ? {is_student}")
print("Your age is: "+str(age)) # combining integer w/ Text

print(f"Today, I ran into a guy named {full_Name}, he was around the age of {age}.")
print(f"If your first name is {first_name} and your last name is {last_Name} your gpa must be at least {gpa}")
#print(type(name))
#print("Hello "+name)