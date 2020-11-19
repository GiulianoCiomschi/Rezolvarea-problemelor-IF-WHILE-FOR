m=eval(input("Dati nr natural m:"))
n=eval(input("Dati nr natural n:"))
puterea=''
if n>m:
    for i in range (1,n+1):
        if(m**i==n):
            puterea='da'
    if puterea=='da':
        print(n,"este putere a lui ",m, sep=" ")   
    else:
          print(n,"nu este putere a lui ",m, sep=" ")
else:       
    print("Eroare")