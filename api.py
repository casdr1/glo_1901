

import requests


URL = "https://pax.ulaval.ca/quoridor/api/v2/"


def lister_parties(idul, secret):
    url = f"https://pax.ulaval.ca/quoridor/api/lister/"
    response = requests.get(url, params={"idul": idul, "secret": secret})
    
    if response.status_code == 200:
        return response.json()
    
    elif response.status_code == 401:
        raise PermissionError(response.json()["message"])
    
    elif response.status_code == 406:
        raise RuntimeError(response.json()["message"])
    
    else:
        raise ConnectionError
    pass


def débuter_partie(idul, secret):
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'sessions/', json={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        id_partie = rep['id']
        etat_partie = rep['état']
        return (id_partie, etat_partie)
    elif rep.status_code == 401:
        raise PermissionError(rep.json()['message'])
    else:
        raise RuntimeError(rep.json()['message'])
    pass


def récupérer_partie(id_partie, idul, secret):
    url = f"https://pax.ulaval.ca/quoridor/api/partie/{id_partie}"
    headers = {'Authorization': f'Bearer {secret}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        partie = response.json()
        return (partie['id'], partie['état'], partie['gagnant'])
    
    elif response.status_code == 401:
        raise PermissionError(response.json()['message'])
    
    elif response.status_code == 406:
        raise RuntimeError(response.json()['message'])
    
    else:
        raise ConnectionError()
    pass


def jouer_coup(id_partie, type_coup, position, idul, secret):
    rep = requests.put(URL+'jouer', auth=(idul, secret), json={'id': id_partie, 'type': type_coup, 'pos': position}).json()
    if 'message' in rep:
        if rep['message'].startswith('La partie est terminée'):
            raise StopIteration(rep['gagnant'])
        elif rep['message'] == 'Le coup est invalide':
            raise RuntimeError(rep['message'])
        else:
            raise PermissionError(rep['message'])
    return rep['id'], rep['état']
    pass
