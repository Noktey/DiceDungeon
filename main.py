import Personnages as p
import Dice as d
import Effet as e


coupEpee1 = e.EffetInfligerDegats('Coup d\'Épée', 1)
coupEpee3 = e.EffetInfligerDegats('Coup d\'Épée Puissant', 3)
sansEffet = e.Effet('Face vierge')

deHero = d.Dice([d.Face(coupEpee1),
                 d.Face(coupEpee1),
                 d.Face(coupEpee1),
                 d.Face(coupEpee3),
                 d.Face(coupEpee3),
                 d.Face(sansEffet)])

hero = p.Hero('Nain', 6, deHero)

coupBoule1 = e.EffetInfligerDegats('Coup de boule', 1)
coupBoule2 = e.EffetInfligerDegats('Coup de boule Puissant', 2)

deMonstre = d.Dice([d.Face(coupBoule1),
                    d.Face(coupBoule1),
                    d.Face(coupBoule2),
                    d.Face(coupBoule2),
                    d.Face(sansEffet),
                    d.Face(sansEffet)])

monstre = p.Monstre('Slime', 5, deMonstre)

while hero.hp != 0 and monstre.hp != 0:
    faceHero = hero.getDicePerso().tirerFace()
    faceMonstre = monstre.getDicePerso().tirerFace()

    print('\n-- Tour du héros --', end='\n\n')

    reroll = 2

    print(faceHero.getEffetFace().nom)

    action = ''
    while action.upper() not in ['REROLL', 'USE']:
        print('Rerolls restants :', reroll)
        action = input('Reroll ou Use ')
        while action.upper() == 'REROLL' and reroll > 1:
            reroll -= 1
            action = ''
            faceHero = hero.getDicePerso().tirerFace()
            print(faceHero.getEffetFace().nom)
            while (action.upper() not in ['REROLL', 'USE']) and reroll > 0:
                print('Rerolls restants :', reroll)
                action = input('Reroll ou Use ')

        if reroll == 1:
            print(faceHero.getEffetFace().nom)

    faceHero.getEffetFace().triggerEffet(monstre)
    print(f'{hero.getNamePerso()}: {hero.getHPPerso()}/{hero.getHPMaxPerso()}')
    print(f'{monstre.getNamePerso()}: {monstre.getHPPerso()}/{monstre.getHPMaxPerso()}')


    if monstre.hp > 0:
        print('\n-- Tour du monstre --', end='\n\n')

        print(faceMonstre.getEffetFace().nom)
        faceMonstre.getEffetFace().triggerEffet(hero)
        print(f'{hero.getNamePerso()}: {hero.getHPPerso()}/{hero.getHPMaxPerso()}')
        print(f'{monstre.getNamePerso()}: {monstre.getHPPerso()}/{monstre.getHPMaxPerso()}')

if hero.hp == 0:
    print('\n>>> C\'est perdu')
else:
    print('\n>>> C\'est gagné')
