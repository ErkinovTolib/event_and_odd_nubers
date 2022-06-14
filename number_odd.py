#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int =1945
#Print the number of odd digits in the variable "var_int".
x = var_int%10
y = var_int//10%10
z = var_int//100%10
c = var_int//1000%10
print(x,z,c)
f = x%2
v = z%2
n = c%2
print(f+v+n)