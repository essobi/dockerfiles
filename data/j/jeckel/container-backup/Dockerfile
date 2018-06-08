FROM alpine:3.5  
MAINTAINER Jeckel <jeckel@jeckel.fr>  
  
RUN apk add --update bash mysql-client && rm -rf /var/cache/apk/*  
  
VOLUME /backups  
  
COPY ./run.sh /usr/local/bin/run.sh  
COPY ./backup.sh /usr/local/bin/backup.sh  
  
CMD ["sh", "/usr/local/bin/run.sh"]

