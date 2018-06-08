FROM alpine:3.2  
MAINTAINER Peter Leitzen <peter@leitzen.de>  
  
ENV OWNCLOUD_VERSION 10.0.4  
ENV OWNCLOUD_PACKAGE owncloud-$OWNCLOUD_VERSION.tar.bz2  
ENV OWNCLOUD_URL https://download.owncloud.org/community/$OWNCLOUD_PACKAGE  
  
ENV TARGET_DIR /usr/share/owncloud  
ENV DIR_OWNER apache  
ENV DIR_GROUP apache  
  
RUN \  
apk add -U \  
apache2 php-apache2 \  
curl \  
php-json php-mysql php-curl php-xml php-xmlreader php-iconv php-ctype php-dom
\  
php-posix php-zip php-zlib php-bz2 php-openssl php-mcrypt \  
php-ftp php-xcache php-pdo_mysql php-gd && \  
rm -fr /var/cache/apk/*  
  
RUN cd /usr/share && \  
curl -LOs $OWNCLOUD_URL && \  
tar xjf $OWNCLOUD_PACKAGE && \  
chown -R $DIR_OWNER:$DIR_GROUP $TARGET_DIR && \  
rm $OWNCLOUD_PACKAGE  
  
ADD owncloud.conf /etc/apache2/conf.d/  
  
WORKDIR $TARGET_DIR  
  
VOLUME ["$TARGET_DIR/config", "$TARGET_DIR/data"]  
VOLUME ["/var/log/apache2", "/tmp"]  
  
EXPOSE 80  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

