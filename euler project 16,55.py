def powerdigitsum(n):
    res=2**n
    digit=str(res)
    print(digit)
    somme=0
    for x in digit:
        somme+=int(x)
    return somme

def palindrome(n):
    if n==inverse_nombre(n):
        return True
    else:
        return False
        
def inverse_nombre(n):
    m=str(n)
    inverse=0
    liste_digits=[]
    for x in m:
        liste_digits.append(int(x))
    for i in range (len(liste_digits)):
        inverse+=liste_digits[i]*10**i
    return inverse 
    
    
def not_lychrel(n,iteration_max):
    iteration=0
    while (iteration<=iteration_max):
        n=n+inverse_nombre(n)
        if palindrome(n):
            return True
        else:
            iteration+=1
    return False
        
        
    
    
def nbre_lychrel(n):
    iteration_max=53
    nombre_lychrel=0
    for i in range (1,n+1): 
        if not_lychrel(i,iteration_max)==False:
            nombre_lychrel+=1
    return nombre_lychrel
        
        
Cecile.Pierrot@inra.fr

open("//etu.ad.univ-lorraine.fr/duchesn13u/Bureau/p022_names.txt","r")