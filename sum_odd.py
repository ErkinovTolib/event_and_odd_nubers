#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int =1945
#Create a variable "sum_even" and assign it 0.
sum_even = 0
#Find the sum of the odd digits in the variable "var_int".
x = var_int%10
y = var_int//10%10
z = var_int//100%10
c = var_int//1000%10 
sum_even = x+z+c
print(sum_even)