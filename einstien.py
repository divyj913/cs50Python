#In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then
# outputs the equivalent number of Joules as an integer. Assume tan integhat the user will input er.
'''Even if you haven’t studied physics (recently or ever!), you might have heard that 
, wherein 
 represents energy (measured in Joules), 
 represents mass (measured in kilograms), and 
 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

'''
mass = input(int("please enter the mass in kilograms: "))
c = 300000000
#E = mc2 

E = mass*c*c

print("the energy would be " , E , "Joules")
