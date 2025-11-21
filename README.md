# 🗂️ Backup-CLI — Python + Docker + CI/CD

Un outil simple en Python permettant de créer automatiquement une sauvegarde d’un dossier vers un dossier `backup/`.

## 🚀 Fonctionnalités
- Sauvegarde automatique avec timestamp
- Simple CLI via `python backup.py source destination`
- Version Docker
- Tests automatisés via GitHub Actions
- Projet d'initiation DevOps

## 🔧 Exécution
### Python
1. Cloner le dépôt
   ```bash
    git clone
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