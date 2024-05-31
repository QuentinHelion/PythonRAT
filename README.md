# PythonRAT

Vous devez réaliser un système de RAT (Remote Administration Tool) exclusivement en Python. Il doit répondre aux exigences
suivantes. Il est composé de deux éléments : **un serveur et un client**. Les deux programmes sont à développer en Python.

Le projet est à réaliser par groupe de 2 **UNIQUEMENT** !

Le rendu du projet est le **30 juin 2024 à 23h59**. Vous devez rendre le code ainsi qu'une vidéo prouvant le bon fonctionnement du
projet.

## Exigences client

- Le client doit communiquer avec le serveur à l'aide d'une socket TCP **chiffrée et sécurisée**.
- Il doit être opérationnel sur les systèmes **Windows** et **Linux**.
- Il doit embarquer les fonctionnalités suivantes :
    - ```help``` : afficher la liste des commandes disponibles.
    - ```download``` : récupération de fichiers de la victime vers le serveur.
    - ```upload``` : récupération de fichiers du serveur vers la victime.
    - ```shell``` : ouvrir un shell (bash ou cmd) interactif.
    - ```ipconfig``` : obtenir la configuration réseau de la machine victime.
    - ```screenshot``` : prendre une capture d'écran de la machine victime.
    - ```search``` : rechercher un fichier sur la machine victime.
    - ```hashdump``` : récupérer la base SAM ou le fichier shadow de la machine.

## Exigences serveur

- Il doit agir à travers une interface interactive lorsque l'agent rentre en contact avec le serveur. Exemple :
```
python server.py
[*] Listening on 8888...
[+] Agent received !
rat > Taper votre commande ici
```
 - Le serveur est en écoute sur un port TCP.


## Fonctionnalités supplémentaires

- Il doit être en mesure d'accepter plusieurs agents en parallèle. Exemple :
```
python server.py
rat >
[+] Agent received !
rat > sessions
[*] Agent 1
[*] Agent 2
rat > interact agent1
rat agent 1 > Taper la commande pour l'agent 1
```
- Implémenter des fonctionnalités supplémentaires pour le client.
- Implémenter des fonctionnalités de contournement d'antivirus.

## Notation
- Qualité du code (fonctions, classes, organisation, etc)
- Fonctionnement du code
- Respect du cahier des charges
- Commentaires au sein du code
  
## Règles
Votre code est analysé dynamiquement par un programme automatique. Il permet de détecter le partage et l'apparition de code
généré par une IA. Toute tentative de triche amenera à une note de 01/20 pour l'ensemble du ou des groupes.
