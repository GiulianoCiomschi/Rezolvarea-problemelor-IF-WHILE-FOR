latura_I=eval(input("Dati lungimile laturilor"))
latura_II=eval(input("Dati lungimile laturilor"))
latura_III=eval(input("Dati lungimile laturilor"))
if(latura_I>0)and(latura_II>0)and(latura_III>0):
    if(latura_I+latura_II>latura_III)and(latura_III+latura_II>latura_I)and(latura_I+latura_III>latura_II):
        if((latura_I==latura_II)and(latura_I!=latura_III))or((latura_II==latura_III)and(latura_II!=latura_I))or((latura_I==latura_III)and(latura_I!=latura_II)):
            print("Este un triunghi isoscel cu laturile:",latura_I, latura_II, latura_III,sep=" ")
        elif (latura_I==latura_II)and(latura_II==latura_III):      
            print("Este un triunghi echilateral cu laturile:",latura_I,sep=" ")
        elif (latura_I!=latura_II)and(latura_II!=latura_III):
            print("Este un triunghi scalen cu laturile:",latura_I, latura_II, latura_III,sep=" ")  
    else:
        print("Erroare, nu exista asa triunghi cu aeste laturi")
else:
    print("Datele sunt gresite")