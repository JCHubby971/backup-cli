# 🗂️ Backup-CLI — Python + Docker + CI/CD
[![CI Backup CLI](https://github.com/JCHubby971/backup-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/JCHubby971/backup-cli/actions/workflows/ci.yml)

## Description
Un outil simple en Python permettant de créer automatiquement une sauvegarde d'un dossier vers un dossier `backup/`.

---

## 🔧 Stack Technique & Compétences

Ce projet couvre plusieurs concepts essentiels du développement et du DevOps :

### 🐍 Python
- Scripts CLI (Command Line Interface)
- Manipulation de fichiers et de dossiers (`os`, `shutil`, `datetime`)
- Gestion d'erreurs et structure d'un module Python
- Projet organisé et reproductible

### 🧪 Tests & Qualité
- Tests unitaires avec **pytest**
- Gestion du PYTHONPATH pour les imports
- Isolation de l'environnement via **venv**
- Bonnes pratiques de validation automatique

### 🐳 Docker & Conteneurisation
- Création d'un **Dockerfile**
- Exécution du programme dans un conteneur
- Gestion des volumes (`-v`) pour manipuler les dossiers source/destination

### 🔁 CI/CD (GitHub Actions)
- Pipeline d'intégration continue
- Installation automatique de Python + pytest
- Exécution des tests à chaque `push` / `pull_request`
- Badge CI pour transparence et professionnalisme

### 🌱 Bonnes pratiques DevOps
- Environnement virtuel isolé (`.venv`)
- `.gitignore` propre
- Documentation claire et structurée
- Code simple, testé, reproductible et portable

---

## 🧰 Installation & Configuration de l'environnement Python

Ce projet utilise un **environnement virtuel Python (venv)** pour garantir une installation propre, reproductible et isolée.
C'est la méthode recommandée pour exécuter correctement le script et les tests.

### 1. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 2. Activer l'environnement

**Windows :**

```powershell
.\.venv\Scripts\activate
```

**Mac / Linux :**

```bash
source .venv/bin/activate
```

Vous devriez voir votre terminal avec le préfixe :

```
(.venv)
```

### 3. Installer les dépendances (tests)

```bash
pip install pytest
```

### 4. Désactiver l'environnement (optionnel)

```bash
deactivate
```

---

### 📌 Facultatif : dépendances de développement

Créer un fichier `requirements-dev.txt` contenant :

```
pytest
```

Installer :

```bash
pip install -r requirements-dev.txt
```

---

## 🔧 Exécution

### Python

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/JCHubby971/backup-cli.git
   cd backup-cli
   ```

2. Exécuter le script de sauvegarde :

   ```bash
   python backup.py /chemin/vers/source /chemin/vers/backup
   ```

---

### Docker

1. Construire l'image Docker

   ```bash
   docker build -t backup-cli .
   ```

2. Exécuter le conteneur

   ```bash
   docker run --rm -v /chemin/vers/source:/source -v /chemin/vers/backup:/backup backup-cli /source /backup
   ```

---

## 🧪 Tests

Exécuter les tests avec pytest :

```bash
pytest
```

---

## 📦 Structure

```
backup.py                # Script principal de sauvegarde
Dockerfile               # Image Docker
.github/workflows/ci.yml # CI/CD GitHub Actions
tests/test_backup.py     # Tests unitaires
requirements.txt         # Dépendances Python
```

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
