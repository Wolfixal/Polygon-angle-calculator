#Calculate the angles of a regular polygon

#Number of sides the polygon has
n = int(input("Insert number of sides your regular polygon has: "))


#Calculates and prints sum of interior angles
print("The sum of interior angles of your polygon =:",(n-2)*180,"°")

#Calculates and prints size of each interior angle
print("Each interior angle =",((n-2)*180)/n,"°")

#Prints the sum of exterior angles
print("The sum of exterior angles is always 360°")

#Calculates and prints size of each exterior angle
print("Each exterior angle =",360/n)