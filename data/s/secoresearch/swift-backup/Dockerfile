FROM python:alpine  
USER root  
  
RUN apk add \--no-cache tar gnupg  
  
# Storage bucket and name for the backup archive file  
ENV BUCKET_NAME "backup"  
ENV BACKUP_NAME "backup"  
# If set, encrypt the archive file using this password  
ENV BACKUP_PASSWORD ""  
# Auth fot the object storage  
ENV OS_AUTH_TOKEN ""  
ENV OS_STORAGE_URL ""  
  
  
ENV PATH_VENV_SWIFT "/venv"  
ENV PATH_BACKUP_SOURCE "/m"  
ENV PATH_BACKUP "/backup"  
ENV FILE_RUN_BACKUP "/run-backup"  
  
ENV PATHS "'$PATH_VENV_SWIFT' '$PATH_BACKUP' '/.gnupg'"  
RUN eval "mkdir -p $PATHS && chmod -R g=u $PATHS"  
RUN python3 -m venv "$PATH_VENV_SWIFT" && \  
. "$PATH_VENV_SWIFT"/bin/activate && \  
pip install python-swiftclient  
  
COPY run "$FILE_RUN_BACKUP"  
RUN chmod ug+x "$FILE_RUN_BACKUP"  
  
USER 10001  
ENTRYPOINT [ "/run-backup" ]  

