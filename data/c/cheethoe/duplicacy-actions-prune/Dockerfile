# This Dockerfile creates an image meant to prune old snapshots for the
$BACKUP_DIR  
# By default this image uses the "keep" options of duplicacy to manage
snapshot  
# pruning. However someone may want to delete a specific set of snapshot tags.  
# To list tags to delete use the TAG env variable and specify tags space
separated:  
# ie.  
# --env "TAG=20180201 20180202". Date format is YYYYMMDD.  
# You may also override the default keep config by either passing KEEP options  
# in the envfile you pass or pass it using --env.  
# ie.  
# --env "KEEP=0:90 4:30"  
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
  
# Default Keep options for this dockerfile  
# This prunes snapshots over 180 days old  
# Keeps 1 snapshot every 30 days for snapshots older than 90 days  
# Keeps 1 snapshot every 7 days for snapshots older than 30 days  
# Keeps 1 snapshot every 2 days for snapshots older than 7 days  
ENV KEEP "0:180 30:90 7:30 2:7"  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

