# backup.py - A simple backup script
import os
import shutil
import argparse
from datetime import datetime

# Function to backup a folder
def backup_folder(source, destination):
    # Check if source folder exists
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source folder not found: {source}")
    
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Generate a timestamped backup folder name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"backup_{timestamp}"
    final_path = os.path.join(destination, backup_name)

    # Copy the source folder to the destination with the new name
    shutil.copytree(source, final_path)
    return final_path

# CLI interface
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Simple Backup CLI")
    parser.add_argument("source", help="Folder to back up")
    parser.add_argument("destination", help="Destination folder for backups")

    # Parse arguments
    args = parser.parse_args()

    # Perform backup
    try:
        path = backup_folder(args.source, args.destination)
        print(f"Backup completed successfully → {path}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Entry point
if __name__ == "__main__":
    main()