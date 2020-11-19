n = eval(input("Dati numarul: "))
s = 0
if ((n != 0) and (n != 1)):
    for i1 in range (1, n+1):
        if n % i1 == 0:
            suma += i1
    if suma == n:
        print("Numarul", n,"este perfect")
    elif suma != n:
        print("Numarul", n,"nu este perfect")