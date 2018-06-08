FROM lsiobase/alpine.nginx:3.6  
# install packages  
RUN \  
apk add --no-cache \  
curl \  
php7-bz2 \  
php7-curl \  
php7-gd \  
php7-gettext \  
php7-dom \  
php7-exif \  
php7-gd \  
php7-iconv \  
php7-mcrypt \  
php7-mysqlnd \  
php7-pdo_mysql \  
php7-xml \  
php7-xmlreader \  
php7-zip  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config  

