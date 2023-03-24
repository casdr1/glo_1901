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
    """Génère un interpréteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut «idul» représentant l'idul du joueur
                   et l'attribut «parties» qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser(prog="main.py", usage="%(prog)s [-h] [-p] idul", description="Quoridor - jeu du TP")
    parser.add_argument("idul", metavar="idul_du_joueur", help="l'idul du joueur")
    parser.add_argument("-p", "--parties", action="store_true", help="Liste des parties existantes" )
   
    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()


def formater_légende(joueurs):
    """Formater la représentation graphique de la légende.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.

    Returns:
        str: Chaîne de caractères représentant la légende.
    """
    légende = 'Légende:\n'
    for i, joueur in enumerate(joueurs):
        nom = joueur['nom']
        murs = '|'*joueur['murs']
        légende += f'{i+1} = {nom:<9}, murs = {murs}\n'
        return légende
    pass


def formater_damier(joueurs, murs):
    """Formater la représentation graphique du damier.

    Args:
        joueurs (list): Liste de dictionnaires représentant les joueurs.
        murs (dict): Dictionnaire représentant l'emplacement des murs.

    Returns:
        str: Chaîne de caractères représentant le damier.
    """
    damier = ['.' for _ in range(9)]
    
    pass


def formater_jeu(état):
    """Formater la représentation graphique d'un jeu.

    Doit faire usage des fonctions formater_légende et formater_damier.

    Args:
        état (dict): Dictionnaire représentant l'état du jeu.

    Returns:
        str: Chaîne de caractères représentant le jeu.
    """
    pass


def formater_les_parties(parties):
    """Formater une liste de parties
    L'ordre rester exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """
    pass


def récupérer_le_coup():
    """Récupérer le coup

    Returns:
        tuple: Un tuple composé d'un type de coup et de la position.
               Le type de coup est une chaîne de caractères.
               La position est une liste de 2 entier [x, y].
    Examples:
        Quel type de coup voulez-vous jouer? ('D', 'MH', 'MV'):
        Donnez la position où appliquer ce coup (x,y): 2,6
    """
    pass
