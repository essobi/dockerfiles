FROM python:2.7-alpine  
MAINTAINER Matt Graham <gadgetmg@gmail.com>  
  
ENV DOCKERIZE_VERSION v0.2.0  
RUN apk --no-cache add ca-certificates g++ gcc git libffi-dev libxml2-dev
libxslt-dev make openssl-dev unrar wget && \  
wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
pip --no-cache-dir install setuptools lxml pyopenssl && \  
apk --no-cache del g++ gcc make wget && \  
git clone \--depth 1 https://github.com/CouchPotato/CouchPotatoServer.git
/couchpotato  
  
COPY config.tmpl /couchpotato/config.tmpl  
  
VOLUME ["/data/couchpotato"]  
  
EXPOSE 5050  
ENTRYPOINT ["dockerize", \  
"-template", "/couchpotato/config.tmpl:/couchpotato/config.ini", \  
"python2", "/couchpotato/CouchPotato.py", \  
"--console_log", \  
"--config_file=/couchpotato/config.ini", \  
"--data_dir=/data/couchpotato"]  

