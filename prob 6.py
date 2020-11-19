
n=eval(input("Dati numarul natural:"))
#a
s1=0
s2=0
for i in range(1,n+1):
    s1=s1+(i**3)
for i in range (1,n+1):
    s2=(s2+i)
s2_=s2**2
if s1>s2_:
    print("suma1",s1,">","suma2",s2_,sep=" ")
elif s2_>s1:
    print("suma1",s1,"<","suma2",s2_,sep=" ")
elif s2_==s1:
    print("suma1",s1,"=","suma2",s2_,sep=" ")

#b

for i in range(1,n+1):
    s1=(s1+(i**2))
s1_=s1*3
for i in range (1,n+1):
    s2=i**3+i**2+(s2+i)  
if s1_>s2:
    print("suma1",">","suma2",sep=" ")
elif s2>s1_:
    print("suma1","<","suma2",sep=" ")
elif s2==s1_:
    print("suma1","=","suma2",sep=" ")
