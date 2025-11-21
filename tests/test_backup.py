# tests/test_backup.py - Tests for backup.py
import os
import sys
from pathlib import Path

# Ajoute la racine du projet au PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from backup import backup_folder  # noqa: E402

# Test to verify backup creation
def test_backup_creation(tmp_path):
    # Créer un dossier source temporaire
    source = tmp_path / "src"
    # Ajouter un fichier au dossier source
    source.mkdir()
    # Créer un fichier dans le dossier source
    (source / "file.txt").write_text("hello")

    # Dossier de destination temporaire
    destination = tmp_path / "dest"

    # Effectuer la sauvegarde
    backup_path = backup_folder(str(source), str(destination))

    # Vérifier que la sauvegarde a été créée avec succès
    assert os.path.exists(backup_path)
    assert os.path.isdir(backup_path)
    assert os.path.exists(os.path.join(backup_path, "file.txt"))