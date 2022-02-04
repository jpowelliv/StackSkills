#   Kelvin to Fahrenheit Project

# Step 1.
''' Let's imagine that the weather reports says that 
the temperature today will be 301 Kelvin.
How should you dress for the day?
Let's create an app that lets us know the temperature in fahrenheit. 
To start, create a variable named kelvin_temp, and set it equal to 301.
Write a comment above that explains this line of code.'''



# Step 2.
''' Finding the temperature in Celsius is similar to Kelvin 
— the only difference is that Celsius is 273.15 degrees less than Kelvin.

Let's convert Kelvin to Celsius by subtracting 273.15 from 
the kelvin_temp variable. Store the result in another variable, 
named celsius_temp.

Write a comment above that explains this line of code.'''




# Step 3.
'''Use this equation to calculate Fahrenheit, 
then store the answer in a variable named fahrenheit_temp.

Fahrenheit = Celsius * (9/5) + 32

In the next step we will round the number saved to fahrenheit_temp. 
Write a comment above that explains this line of code.'''




# Step 4.
'''Use the print() function to print the value of fahrenheit_temp.
In our next step we are going to see what we can do to make sure that
our number is a whole number by rounding down.
The value you printed should begin with 82.13'''




# Step 5.
'''Import the Math library. We are going to have to make use of its 
methods. On line one add import math

5. As we have just seen, when you convert from Celsius to Fahrenheit, 
you often get a decimal number. 
Go ahead and remove the print command from step 4.

Use the .floor() method from the Math library to round down 
the Fahrenheit temperature. 
Save the result to the fahrenheit_temp variable. 
Check out the documentation for math.floor() 
here: http://bit.ly/javascript-math-floor.
 This will round your decimal down no matter what the value.
 Other methods from the Math library you might try out are .round()
 and ceil(). Write a comment above that explains this line of code.'''





# Step 6.
'''Use the print() function and string concatenation to log 
the temperature in fahrenheit_temp to the console to create 
the message as follows: The temperature is TEMPERATURE degrees Fahrenheit. 
TEMPERATURE should be determined by the value of fahrenheit_temp.'''


# Code:

# import math
import math

# create a variable named kelvin_temp, and set it equal to 301
kelvin_temp = 301

# convert Kelvin to Celsius 
# subtract 273.15 from kelvin_temp variable
# Store the result in another variable, named celsius_temp
celcisus_temp = kelvin_temp - 273.15

# calculate Fahrenheit, store in a variable named fahrenheit_temp
fahrenheit_temp = celcisus_temp * (9 / 5) + 32

# print answer
print(fahrenheit_temp)

# round the value of fahrenheit_temp down
fahrenheit_temp  = math.floor(fahrenheit_temp)

# use the print() function and string concatenation to log the temperature in fahrenheit_temp
# message "The temperature is TEMPERATURE degrees Fahrenheit."
print("The Tempature is", (fahrenheit_temp), "degress fahrenheit")
