from fractions import Fraction
a=eval(input("Dati nr natural a:"))
b=eval(input("Dati nr natural b:"))
c=eval(input("Dati nr natural c:"))
d=eval(input("Dati nr natural d:"))
suma=Fraction(a,b)+Fraction(c,d)
produsul=Fraction(a,b)*Fraction(c,d)
print("suma fractiilor este", suma, sep=" ")
print("produsul fractiilor este", produsul, sep=" ")