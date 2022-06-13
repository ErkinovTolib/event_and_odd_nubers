#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 1456
#Print the number of even digits in the variable "var_int".
y = var_int%10
x = var_int//100%10
print(y,x)