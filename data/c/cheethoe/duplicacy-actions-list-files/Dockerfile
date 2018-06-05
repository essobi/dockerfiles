# This Dockerfile creates an image meant to list files in a snapshot for the
$BACKUP_DIR  
# To list files for a specific tag use --env "TAG=20180201". Date format is
YYYYMMDD.  
From cheethoe/duplicacy-base:2.0.10  
LABEL maintainer="Michael Hsu"  
  
# Environment Vars  
ENV BACKUP_DIR "/backup"  
ENV SNAPSHOT_ID "testing"  
ENV STORAGE_URL "sftp://127.0.0.1"  
ENV THREADS "4"  
# Encryption password  
ENV DUPLICACY_PASSWORD ""  
# SFTP  
# This will not actually work, duplicacy developer states  
# it can only read the ssh password from the keyring.  
ENV DUPLICACY_SSH_PASSWORD ""  
ENV DUPLICACY_SSH_KEY_FILE ""  
# Dropbox  
ENV DUPLICACY_DROPBOX_TOKEN ""  
# Amazon S3  
ENV DUPLICACY_S3_ID ""  
ENV DUPLICACY_S3_SECRET ""  
# BackBlaze B2  
ENV DUPLICACY_B2_ID ""  
ENV DUPLICACY_B2_KEY ""  
# Microsoft Azure  
ENV DUPLICACY_AZURE_KEY ""  
# Google Drive  
ENV DUPLICACY_GCD_TOKEN ""  
# Microsoft OneDrive  
ENV DUPLICACY_ONE_TOKEN ""  
# Hubic  
ENV DUPLICACY_HUBIC_TOKEN ""  
WORKDIR $BACKUP_DIR  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

