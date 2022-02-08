#   Cat Convertor
# Challenge: Convert Your Age to Cat Years
#  The first two years of a cat's life count as 25 cat years each.
#  Each year following equates to 4 cat years.

# Step 1.
''' Begin by creating a variable named my_age,
and set it equal to your age as a number. 
Write a comment that explains this line of code.'''


# Step 2.
''' Next, create a variable named early_years and save the value 2 to it.
Note, the value saved to this variable will change. 
Write a comment that explains this line of code.'''


# Step 3.
'''Use the multiplication assignment operator *= to multiply 
the value saved to early_years by 25 and reassign it to early_years. 
This will account for the first two years of a cats life where they 
experience accelerated growth. 
Write a comment that explains this line of code.'''


# Step 4.
'''Since we already accounted for the first two years, 
take the my_age variable, and subtract 2 from it.
Set the result equal to a variable called later_years.
We'll be changing this value later.
Write a comment that explains this line of code.'''


# Step 5.
'''Multiply the later_years variable by 4 to calculate 
the number of cat years accounted for by your later years.
Use the multiplication assignment operator *= 
to multiply and assign in one step. 
Write a comment that explains this line of code.'''


# Step 6.
'''If you'd like to check your work at this point,
print early_years and later_years. Are the values what you expected?'''


# Step 7.
'''Go ahead and delete the print logs from step 6.
Add early_years and later_years together, and store
that in a variable named my_age_in_cat_years.'''


# Step 8.
'''Save the value of your name to the variable my_name. 
Write your name as a string and store the result in a 
variable called my_name. 
Write a comment that explains this line of code.'''


# Step 9.
'''Print a statement that displays your name and age in cat years. 
Use string concatenation to display the value in the following sentence:

* My name is NAME. I am HUMAN AGE years old in human years 
which is CAT AGE years old in cat years. *

Replace  "NAME" with my_name, "HUMANE AGE" with my_age, 
and  "CAT AGE" with my_age_in_cat_years in the sentence above.'''

# Code:
# create variable named 'my_age' ,and set it equal to your age as a number 
my_age = 26

# create a variable named 'early_years' and save the value '2' to it
early_years = 2


# multiplication assignment operator *= to multiply 
# the value saved to 'early_years' by '25' and reassign it to early_years
early_years *=25 


# take the my_age variable, and subtract '2' from it
# cat's first two years name it 'later_years`
later_years = my_age- 2


# print early_years and later_years
#print(early_years)
#print(later_years)


# delete (comment out) the print logs from step 6
# Add early_years and later_years together & name it my_age_in_cat_years
my_age_in_car_years = early_years+ later_years


# Save the value of your name to the variable my_name
my_name = "Wiley"



#  print a string that says 
# `My name is NAME. I am HUMAN AGE years old in human years 
# which is CAT AGE years old in cat years.`
print("My name is ", my_name + " . I am ", my_age, "years old in human years which is ", my_age_in_car_years, " years old in cat years. ")
print("My name is " + my_name + " . I am " + str(my_age) + "years old in human years which is " + str(my_age_in_car_years) + " years old in cat years. ")