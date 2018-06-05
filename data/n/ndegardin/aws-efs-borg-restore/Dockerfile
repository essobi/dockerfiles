FROM alpine  
MAINTAINER Nicolas Degardin <degardin.n@gmail.com>  
  
RUN apk add --update --no-cache borgbackup wget ca-certificates bash  
RUN mkdir -p /mnt/source  
RUN mkdir -p /mnt/backup  
  
COPY restore.sh /usr/bin/restore  
  
ENTRYPOINT ["restore"]

