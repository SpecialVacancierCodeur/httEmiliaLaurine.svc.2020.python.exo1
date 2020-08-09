#Saisie des coefficients
a = 2
b = 5
c = 3

#Calcul du discriminant
D = (b^2)-(4*a*c)

if D<0:
   print ("Pas de solutions")

elif D == 0:
   x = b/(2*a)
   print ("Une solution double")
   print (x)
   
else:
   x1 = (-b-pow(D, 1/2))/(2*a)
   x2 = (-b+pow(D, 1/2))/(2*a)
   print ("Deux solutions 'x1' et 'x2' ")
