n=int(input("dati n de zile din luna="))
if (n==28):
    print("Februarie")
elif (n==29):
    print("februarie ,an bisect")
elif (n==30):
    print("Aprilie,Iunie,Septembrie,Noiemrie")
elif (n==31):
    print("Ianuarie,Martie,Mai,Iulie,August,Octombrie,Decembrie")
elif (n<28)or(n>31):
    print("Nu exista asa luna")
