n=eval(input("n="))
p=1
s=0
for i in range(1,n+1,1) :
    p*=i
    s+=p
print ("Suma este =",s)