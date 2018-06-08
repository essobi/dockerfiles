FROM lsiobase/alpine.nginx:3.6  
MAINTAINER saghul  
  
# NOTE: this is not an official LinuxServer.io build.  
# install packages  
RUN \  
apk add --no-cache \  
curl \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-iconv \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-opcache \  
php7-pdo_sqlite \  
php7-session \  
php7-xml \  
unzip  
  
# copy local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config  

