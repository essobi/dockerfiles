FROM lsiobase/alpine  
  
LABEL maintainer "zaggash"  
  
ENV SEMAPHORE_VERSION=v2.2.0  
ENV DATADIR="/config/databases"  
ENV GIN_MODE=release  
ENV MYSQL_HOST="127.0.0.1:3306"  
ENV MYSQL_ROOT_PASSWORD=""  
ENV MYSQL_SEMAPHORE_USER="semaphore"  
ENV MYSQL_SEMAPHORE_PASSWORD=""  
# install ansible/semaphore  
RUN \  
apk add --no-cache --virtual=build-dependencies \  
curl && \  
  
apk add \--no-cache \  
mariadb \  
mysql-client \  
pwgen \  
python \  
git \  
ansible && \  
  
curl -q -L \  
https://github.com/ansible-
semaphore/semaphore/releases/download/${SEMAPHORE_VERSION}/semaphore_linux_amd64
> /usr/bin/semaphore && \  
chmod +x /usr/bin/semaphore && \  
  
apk del --purge \  
build-dependencies && \  
rm -rf /var/cache/apk/* /tmp/*  
  
# copy local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 3000  
VOLUME /config  

