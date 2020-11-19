n = eval(input("Dati virsta lui Mihai: "))
s = 1
s2 = 0

if n<20:
    for i in range (1,n+1):
        s= s*2 + i
    print("La", n,"ani primeste", s,"dolari")
    if s <= 100:
         print("Mihai nu primeste mai mult de 100 dolari")
    if s >= 100:
         s2 = (s2*2) + i
         print("Mihai primeste mai mult de 100 dolari la", i,"ani")