FROM alpine:3.5  
MAINTAINER Andrew Usov "andrew.usov@youdowell.com"  
ENV BACKUP_DIR /data/mysqldump  
  
RUN set -x && \  
apk add --no-cache \  
python2 \  
groff \  
less \  
bash \  
mysql-client && \  
apk --no-cache add --virtual=.build-deps py2-pip && \  
pip --no-cache-dir install awscli && \  
apk del .build-deps && rm -rf /tmp/*  
  
ADD ["mysql-backup.sh", "/usr/local/bin/"]  
CMD ["mysql-backup.sh"]  

