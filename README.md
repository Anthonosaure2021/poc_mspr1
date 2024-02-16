Il s'agit d'un POC pour la MSPR1, je vous propose ceci que l'on doit mettre en place pour notre rattrapage.

# Qu'est ce cette solution ?

Il s'agit d"une application a déployer sur le SRVCL dans la partage samba, je m'explique: 
- Chaque SRVCL aura un partage samba de crée afin d'y déposer le script (avec ansible ou autre), le dossier "script" et harvester.py seront donc dans /srv/partage (ou autre dossier mais il faudra modifier les scripts en conséquents). \
Le script Harvester.py est notre application qui va se charger de scanner le réseau en appellant les scripts "nmap_client.py" dans /script qui lui appelle nmap_serveur.py qui est sur le SRVCL.



# Comment fonctionne la solution ?
\




Au jour du vendredi 16/02 à 12h16, la partie "application web" n'a pas été entammée.
