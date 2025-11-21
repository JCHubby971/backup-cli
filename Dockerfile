# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY backup.py .

# Entry point to run the backup script
ENTRYPOINT ["python", "backup.py"]

# Exemple d’exécution en Docker :
# docker build -t backup-cli .
# docker run --rm -v /path/to/source:/source -v /path/to/destination:/destination backup-cli /source /destination