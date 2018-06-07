FROM alpine  
MAINTAINER Nicolas Degardin <degardin.n@gmail.com>  
  
RUN apk add --update --no-cache borgbackup wget ca-certificates nfs-utils  
RUN mkdir -p /mnt/source  
RUN mkdir -p /mnt/backup  
  
COPY backup.sh /usr/bin/backup  
  
ENTRYPOINT ["backup"]

