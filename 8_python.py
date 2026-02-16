
life = 7
mot_mystere = 'Plasma'
mot_public = '_' * len(mot_mystere)

while life > 0 and mot_mystere != mot_public:
    lettre = input('Entrez une lettre : ')

    if lettre in mot_mystere:
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
    else:
        life -= 1

    if mot_public == mot_mystere:
        print("Bravo ! Le mot est", mot_mystere)
    elif life == 0:
        print("Perdu ")
    else:
        print("Vous avez", life, "vies")
        print("Le mot est :", mot_public)
