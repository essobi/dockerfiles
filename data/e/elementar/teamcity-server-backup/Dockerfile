FROM alpine:latest  
MAINTAINER Elementar Sistemas <contato@elementarsistemas.com.br>  
  
# assumes the local backup dir is the official teamcity server image default  
ENV LOCAL_BACKUP_DIR /data/teamcity_server/datadir/backup/  
  
# installs dependencies and copies the entrypoint script  
RUN apk add --no-cache bash curl py-pip && pip install awscli  
COPY ./tc-backup.sh /usr/local/bin/  
  
ENTRYPOINT ["/usr/local/bin/tc-backup.sh"]  

