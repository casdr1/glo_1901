"""Module Quoridor

Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_légende - Formater la représentation graphique du damier.
    * formater_damier - Formater la représentation graphique de la légende.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
import argparse


def analyser_commande():
   
    
    parser = argparse.ArgumentParser(prog="main.py", usage="%(prog)s [-h] [-p] idul", description="Quoridor - jeu du TP")
    parser.add_argument("idul", metavar="idul_du_joueur", help="l'idul du joueur")
    parser.add_argument("-p", "--parties", action="store_true", help="Liste des parties existantes" )
    return parser.parse_args()


def formater_légende(joueurs):
    
    
    max_nom = max([len(joueur["nom"]) for joueur in joueurs])
    max_murs = max([joueur["murs"] for joueur in joueurs])
    légende = "Légende:\n"
    for i, joueur in enumerate(joueurs):
        nom = joueur["nom"]
        murs = '|'*joueur["murs"]
        espaces = " " * (max_nom - len(nom))
        légende += f"   {i+1}={nom},{espaces} murs={murs:>{max_murs}}\n"
    return légende
    pass


def formater_damier(joueurs, murs):
   

    damier = [['.' for _ in range(9)] for _ in range(9)]
    num_joueur = 1
    for joueur in joueurs:
        x, y = joueur["pos"]
        damier[9-y][x-1] = str(num_joueur)
        num_joueur += 1
    

    for mur_hrz in murs['horizontaux']:
        x, y = mur_hrz
        damier[x][y] = '-------'
    

    for mur_vrt in murs['verticaux']:
        x, y = mur_vrt
        damier[x][y] = '|'


    chaine_damier = "   "+'-'*35 + '\n'
    for i, ligne in enumerate(damier):
        num_ligne = 9 - i
        chaine_ligne = f"{num_ligne} | {'   '.join(ligne)} |\n"
        chaine_damier += chaine_ligne
        chaine_damier += '  '+'|'+' '*35+'|''\n'
    chaine_damier += '--|'+'-'*35 + '\n'
    chaine_damier += '  | 1   2   3   4   5   6   7   8   9\n'
    return chaine_damier
    pass


def formater_jeu(état):
    
    
    damier = formater_damier(état['murs'], état['joueurs'])
    légende = formater_légende(état['joueurs'])
    plateau = ''
    for i, ligne in enumerate(damier):
        plateau += ligne + '\t' + légende[i] + '\n'
    return plateau
    pass


def formater_les_parties(parties):
    
    
    parties_format = []
    for i, partie in enumerate(parties):
        id_partie = i + 1
        date = partie["date"]
        joueurs = ' vs '.join(partie['joueurs'])
        gagnant = partie['gagnant'] or 'en cours'
        partie_format = f"{id_partie}: {date}, {joueurs}, gagnant: {gagnant}"
        parties_format.append(partie_format)
    return '\n...\n'.join(parties_format)
    pass


def récupérer_le_coup():
    
    
    typeshot = input("Quel type de coup voulez-vous jouer? ('D', 'MH'. 'MV'): ")
    while typeshot not in ['D', 'MH', 'MV']:
        typeshot = input("Coup invalide. Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'): ")
    
    pos_str = input("Entrez la position où vous souhaitez appliquer le coup (x,y): ")
    pos_liste = pos_str.split(',')
    while pos_liste[0].isdigit or pos_liste[1].isdigit() is False:
        pos_str = input('Position non valide, entrez une position (x,y) valide: ')
        pos_liste = pos_str.split(',')
    position = [int(pos_liste[0]), int(pos_liste[1])]
    return typeshot, position
    pass
