#Exo 1: Ecrire un programme qui demande à l’utilisateur 3 nombres entiers positifs et plus petits que 40000, puis effectue la moyenne de ces 
# trois nombres et affiche la valeur de cette moyenne. Le code n'effectuera pas de vérification concernant l'intervalle de 0 à 40000.

#pseudo code
#a <- entier
#b <- entier
#c <- entier
#i <- a +b+c
#Pour i <- jusqu’à 40000
#Ecrire i 


#ci dessous solution exo1
a=10
b=20
c=50
i=(a+b+c)/3
if (i> 0) and (i<40000):
    print(i)
else:
    print("too bad")


#autre solution
while True:
    a=int(input("Entrez un premier nombre"))
    if a> 0 and a<40000:
        break #le break sert a sortir de la boucle cad si les conditions du if ne sont pas remplies, sortir de la boucle et aller au print
    print("le nombre n'est pas valide")
b=int(input("Entrez un deuxième nombre"))
c=int(input("Entrez un troisième nombre"))
total_notes = 3
moyenne =(a+b+c)/ total_notes


#autre solution en utilisant une liste
a=b=c=0
somme=moyenne=0
liste=[a,b,c]
for indice in range (0,3):
    while True:
        liste[indice]=int(input("Entrez un nombre"))
        if (liste[indice] > 0 and liste[indice]<40000):
            somme+=(liste[indice])
            break #le break sert a sortir de la boucle cad si les conditions du if ne sont pas remplies, sortir de la boucle et aller au print
        print("le nombre n'est pas valide")


# test d'une solution : for i in range(0,40000): pas de boucle for et in range car déroule tous les nombres jusqu'à 40000
#   print (i)


#Exo 2: Ecrire un programme qui demande à l'utilisateur de saisir un nombre entier et qui 
# indique selon le cas : Ce nombre est positif ou nul. Ce nombre est négatif 
#ci dessous solution exo2
nombre = int(input("saisir un nombre"))
if nombre >= 0 :
    print("Ce nombre est positif ou nul")
else:
    print("Ce nombre est négaif")


#Exo 3: Ecrire un programme qui réalise la saisie par l’utilisateur d’un nombre et qui indique 
# si ce nombre est divisible par 3 ou pas. On pourra par exemple utiliser le modulo (%)
# #ci dessous solution exo3 
nombre1 = int(input("saisir un nombre"))
nombreDivisible = nombre1 % 3
if nombreDivisible == 0:
    print("ce nombre est divisible par 3")
else:
    print("ce nombre n'est pas divisible par 3")



#Exo 4: Écrire un programme qui détermine la valeur de la racine carrée d’un entier sans 
# jamais utiliser la fonction racine carrée. 
#On procédera par approximation successive. 
#Prenons par exemple la racine carrée de N=10. 
#On teste la valeur 5. 
#5x5 = 25 résultat supérieur à 10. 
#Donc le nombre recherché sera compris entre 0 et 5 
#On teste 2,5. 2,5 x 2,5 = 6,25 qui est inférieur à 10. 
#Donc le nombre recherché sera compris entre 2,5 et 5. 
#On teste donc (2,5+5)/2= 3,75. 3,75x3,75 vaut 14,0625 donc plus grand que 10. 
#Le nombre recherché est donc entre 2,5 et 3,75. 
#On teste (2,5+3,75)/2 qui vaut 3,125. 3,125*3,125 vaut 9,765625. 
#Donc le nombre recherchée est entre 3,125 et 3,75. On teste (3,125+3,75)/2 etc. 
#On remarque qu’à chaque fois, on obtient deux nombres NBas et NHaut qui encadre la valeur 
#de la racine carrée. 
#L’intervalle entre ces deux nombres devient de plus en plus petit. 
# On arrêtera les itérations du calcul lorsque la différence entre Nbas et NHaut 
# sera plus petit que 0,001.
#ci dessous solution exo3
#etape 1: prendre 10 comme exemple de nombre maximum
n=10
#etape 2: mentionner la saisie de l'utilisateur en créant une vadiable nommée y
y=int(input("saisir un nombre"))
#etape 3: définir une variable qui multiplie le y par lui même 
a=y*y
#etape 4: créer une boucle while pour itérer chaque fois que l'utilisateur écrit un nombre
#préciser que a ne doit pas dépasser n car une racine carré ne peut pas surpasser le nb duquel il est la racine carré
while a<n:
    #etape 5: pour faire le tatonnement, définir une variable qui multiplie la valeur de y en 2 puis multiplier cette valeur
    x=(y/2)*2
    #etape 6: definir la condition qui dit que les itérations doivent s'arreter quand la différence ente y et x est inférieur à 0.01
    if y-x ==0.001:
        continue
    print(x)

n = float(input("saisir un nombre"))
bas = 0.0
haut = n
moyenne = (haut+bas)/2
while ((haut-bas) > 0.001):
    if (moyenne * moyenne > n):
        haut = moyenne
    else(moyenne * moyenne<n):
        bas = moyenne
