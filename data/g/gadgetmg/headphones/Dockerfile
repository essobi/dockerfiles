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
git clone \--depth 1 https://github.com/rembo10/headphones.git /headphones  
  
COPY config.tmpl /headphones/config.tmpl  
  
VOLUME ["/data/headphones"]  
  
EXPOSE 8181  
ENTRYPOINT ["dockerize", \  
"-template", "/headphones/config.tmpl:/headphones/config.ini", \  
"python2", "/headphones/Headphones.py", \  
"--config=/headphones/config.ini", \  
"--datadir=/data/headphones"]  

