# ![LiveCampus](https://cdn.prod.website-files.com/66153b9f3cb891501ecbf3e3/66154208e9b332c598edfd0e_logo-lc.png)

## MDV P25 - Projet d'Automatisation

### Développeurs :
- Matthieu Fanget
- Ben Yamine Ali
- Aymeric Surre

---

### **But du projet :**
Ce projet a pour objectif de développer un script Python capable d'automatiser plusieurs tâches liées à la gestion d'environnements virtuels et de conteneurs. En s'appuyant sur des outils comme **VirtualBox** et **Docker**, le script permet de :

- **Détecter l'OS** sur lequel il est exécuté.
- **Vérifier la présence de VirtualBox** et afficher un lien pour le téléchargement si nécessaire.
- **Vérifier la présence de Docker** et activer son service si besoin, ou fournir un lien pour l'installation.
- **Créer une machine virtuelle (VM)** avec 2 CPU et un ISO Linux attaché, via VirtualBox.
- **Créer des conteneurs Docker** avec plusieurs options (Ubuntu, Debian, Fedora, etc.), et permettre le rattachement de volumes persistants.

Le projet inclut également :
- L'utilisation de **tests unitaires** (via `pytest`) pour chaque fonction développée.
- L'intégration d'un **workflow GitHub Actions** permettant l'exécution automatique des tests à chaque push.
- La **notification par email** à l'équipe de développement et à l'intervenant après chaque push réussi ou échoué.

---

### **Technologies utilisées :**
- **Python 3**
  - Modules : `os`, `platform`, `subprocess`, `colorama`
- **VirtualBox**
- **Docker**
- **GitHub Actions**
- **pytest** pour les tests unitaires
- **colorama** pour la colorisation des sorties terminales

---

### **Comment utiliser ce projet :**
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/AyDev38/lvcampus-env-2.git
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Exécutez le script principal :
   ```bash
   python main.py
   ```

4. Pour lancer les tests :
   ```bash
   pytest
   ```

5. Pour plus de détails sur les fonctionnalités, référez-vous à la documentation du projet.

---

### **Liens utiles :**
- [Télécharger VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Télécharger Docker](https://docs.docker.com/get-docker/)

