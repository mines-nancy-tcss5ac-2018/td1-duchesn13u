alphabet_maj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


fichier=open("D:/Mines nancy/informatique/semestre 5/p022_names.txt","r")

score_mot=0
numéro_mot=1
total=0
x=fichier.readline()
for y in x:
    if y==',':
        total=total+score_mot*numéro_mot
        score_mot=0
        numéro_mot+=1
        
    for i in range (26):
        if y==alphabet_maj[i]:
            score_mot+=i+1

print(total)


fichier.close
