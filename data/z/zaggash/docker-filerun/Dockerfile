FROM lsiobase/xenial  
MAINTAINER zaggash  
  
# environment variables  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV FILERUN_PATH="/config/www/filerun"  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# update apt and install packages  
RUN \  
apt-get update && \  
apt-get install -y \  
curl \  
logrotate \  
ca-certificates \  
git \  
logrotate \  
nginx \  
openssl \  
unzip \  
mysql-client \  
graphicsmagick \  
ffmpeg \  
php7.0 \  
php7.0-fpm \  
php7.0-common \  
php7.0-curl \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-exif \  
php7.0-xml \  
php7.0-zip \  
php7.0-gd \  
php7.0-opcache && \  
  
apt-get install -y \  
php7.0-dev && \  
  
# install IonCube  
curl -O
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
&& \  
tar xvfz ioncube_loaders_lin_x86-64.tar.gz && \  
PHP_EXT_DIR=$(php-config7.0 --extension-dir) && \  
cp "ioncube/ioncube_loader_lin_7.0.so" $PHP_EXT_DIR && \  
echo "zend_extension=ioncube_loader_lin_7.0.so" >>
/etc/php/7.0/fpm/conf.d/00_ioncube_loader_lin_7.0.ini && \  
rm -rf ioncube ioncube_loaders_lin_x86-64.tar.gz && \  
  
# configure nginx  
echo 'fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;' >> \  
/etc/nginx/fastcgi_params && \  
rm -f /etc/nginx/conf.d/default.conf && \  
  
# cleanup  
apt-get autoremove --purge -y \  
php7.0-dev && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/* \  
/usr/lib/x86_64-linux-gnu/libfakeroot/ \  
/etc/logrotate.d/php7.0-fpm \  
/etc/logrotate.d/nginx  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config  

