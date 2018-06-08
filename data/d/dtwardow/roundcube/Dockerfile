FROM php:5-apache  
MAINTAINER Dennis Twardowsky <twardowsky@gmail.com>  
  
ENV WWW_DIR /var/www/html  
ENV DATA_DIR /data  
ENV SCRIPTS_DIR /opt/scripts  
  
RUN apt-get update && \  
apt-get -y install wget sudo gettext-base sqlite3 && \  
apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmysqlclient-dev \  
libsqlite3-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install mysql && \  
apt-get clean  
  
# install roundcube  
RUN wget "http://sourceforge.net/projects/roundcubemail/files/latest/download"
-O roundcubemail.tar.gz && \  
tar xvf roundcubemail.tar.gz -C / && \  
rm roundcubemail.tar.gz; \  
mv /roundcube* /roundcube && \  
mv /roundcube/* ${WWW_DIR}  
  
# fix rights  
RUN chmod a+rw ${WWW_DIR}/temp/; \  
chmod a+rw ${WWW_DIR}/logs/  
  
# add config  
ADD assets/conf/* /opt/config/  
ADD assets/scripts/* ${SCRIPTS_DIR}/  
ADD assets/www/* ${WWW_DIR}/  
RUN chmod -R u+x ${SCRIPTS_DIR}  
  
VOLUME ["${DATA_DIR}"]  
  
EXPOSE 80  
ENTRYPOINT ["/opt/scripts/entrypoint.sh"]  
CMD ["app:start"]  
  

