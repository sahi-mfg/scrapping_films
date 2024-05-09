## Scrapping de films, leur notes et les critiques [SensCritique](https://www.senscritique.com/films)

### Comment lancer le script ?

- Installer les dépendances : `pip install -r requirements.txt` ou `make install` si vous avez `make` d'installé

- Lancer le script : `python main.py` ou `make run` si vous avez `make` d'installé

- pour exécuter le scripts tous les jours entre 8h et 10h : il faut ajouter une tâche cron `crontab -e` et ajouter la ligne suivante `0 8-10 * * * python ~/Projet_ISE/main.py` (en remplaçant le chemin par le votre). Ceci fonctionne sur linux et macos, pour windows il faut utiliser le planificateur de tâches (je ne sais pas comment ça fonctionne).
