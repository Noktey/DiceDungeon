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
        print(hero.hp, '->', hero.hp + hero.soin)
        hero.soigner(hero)

    else:
        print(f'Le {hero.name} attaque le {monstre.name}')
        print(monstre.hp, '->', monstre.hp - hero.dmg)
        hero.infligerDegats(monstre)

    if monstre.hp > 0:
        print('\n-- Tour du monstre --', end='\n\n')

        print(f'Le {monstre.name} attaque le {hero.name}')
        print(hero.hp, '->', hero.hp - monstre.dmg)
        monstre.infligerDegats(hero)

if hero.hp == 0:
    print('\n>>> C\'est perdu')
else:
    print('\n>>> C\'est gagné')



