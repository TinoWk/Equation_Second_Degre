import numpy as np
import cmath

#equation
def equation(a,b,c):
    r1initial,r2initial,disc=0,0,0
    #disrminant 
    disc=(b**2)-4*a*c
    if a!=0:
        r2=r2initial
        r1=r1initial
    

            #conditions
        if disc<0:
             print("Discriminant Négatif !")
             ajustement=cmath.sqrt(disc)
             r1=(-b+ajustement)/(2*a)
             r2=(-b-ajustement)/(2*a)       
        else :
            if disc>0:
                print("Discriminant positif!")
                r1=(-b+np.sqrt(disc)/(2*a))
                r2=(-b-np.sqrt(disc)/(2*a))
            else:
                if disc==0:
                    print("Discriminant nul! ")
                    r1=r2=(-b/(2*a))
        return r1,r2
    else:
        print(" Il s'agit d'une équation du premier dégré !")
        if b!=0:
           return (-c/b)
        else:
            print(" ZéroDivisionErreur")

print(equation(0,0,1))