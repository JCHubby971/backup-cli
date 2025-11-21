# 🗂️ Backup-CLI — Python + Docker + CI/CD
[![CI Backup CLI](https://github.com/JCHubby971/backup-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/JCHubby971/backup-cli/actions/workflows/ci.yml)

## Description
Un outil simple en Python permettant de créer automatiquement une sauvegarde d’un dossier vers un dossier `backup/`.

## 🚀 Fonctionnalités
- Sauvegarde automatique avec timestamp
- Simple CLI via `python backup.py source destination`
- Version Docker
- Tests automatisés via GitHub Actions
- Projet d'initiation DevOps

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

Ce projet n'utilise pas de dépendances externes pour l'outil lui-même,
mais nécessite `pytest` pour lancer les tests unitaires :

```bash
pip install pytest
```

### 4. Désactiver l'environnement (optionnel)

```bash
deactivate
```

---

### 📌 Facultatif : dépendances de développement

Si vous préférez installer les outils de test via un fichier dédié :

Créer un fichier `requirements-dev.txt` contenant :

```
pytest
```

Installer :

```bash
pip install -r requirements-dev.txt
```

## 🔧 Exécution
### Python
1. Cloner le dépôt
   ```bash
    git clone https://github.com/JCHubby971/backup-cli.git
    cd backup-cli
    ```
2. Exécuter le script de sauvegarde
   ```bash
    python backup.py /chemin/vers/source /chemin/vers/backup
   ```  
### Docker
1. Construire l’image Docker
   ```bash
    docker build -t backup-cli .
   ```

2. Exécuter le conteneur
   ```bash
    docker run --rm -v /chemin/vers/source:/source -v /chemin/vers/backup:/backup backup-cli /source /backup
   ```
## 🧪 Tests
Exécuter les tests avec pytest :
```bash
pytest
```

## 📦 Structure
backup.py - Script principal de sauvegarde  
Dockerfile - Fichier de configuration Docker
.github/workflows/ci.yml - Configuration CI/CD GitHub Actions
tests/test_backup.py - Tests unitaires avec pytest
requirements.txt - Dépendances Python

## 📄 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.