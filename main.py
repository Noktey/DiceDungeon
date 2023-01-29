import Personnages as p

hero = p.Hero('Nain', 6, 2, 1)

monstre = p.Monstre('Slime', 5, 2, 0)

while hero.hp != 0  and monstre.hp != 0:
    print('\n-- Tour du héros --', end='\n\n')
    action = ''
    while action.upper() not in ['SOIGNER', 'ATTAQUER']:
        action = input('Soigner ou Attaquer ')

    if action.upper() == 'SOIGNER':
        print(f'Le {hero.name} se soigne')
        print(hero.hp, '-> ', end='')
        hero.soigner(hero)
        print(hero.hp)

    else:
        print(f'Le {hero.name} attaque le {monstre.name}')
        print(monstre.hp, '-> ', end='')
        hero.infligerDegats(monstre)
        print(monstre.hp)

    if monstre.hp > 0:
        print('\n-- Tour du monstre --', end='\n\n')

        print(f'Le {monstre.name} attaque le {hero.name}')
        print(hero.hp, '-> ', end='')
        monstre.infligerDegats(hero)
        print(hero.hp)

if hero.hp == 0:
    print('\n>>> C\'est perdu')
else:
    print('\n>>> C\'est gagné')



