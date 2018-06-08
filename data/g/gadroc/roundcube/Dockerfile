FROM php:5.6-apache  
  
EXPOSE 80  
  
ENV PACKAGES="aspell aspell-en enchant libicu52 libmcrypt4 mysql-client"  
ENV BUILD_PACKAGES="libenchant-dev libicu-dev libmysqlclient-dev
libmysqlclient-dev libmcrypt-dev wget"  
  
RUN . /etc/apache2/envvars && \  
apt-get update && \  
apt-get install -y $PACKAGES $BUILD_PACKAGES && \  
docker-php-ext-install pdo_mysql mcrypt mbstring intl exif zip enchant && \  
wget
"https://github.com/roundcube/roundcubemail/releases/download/1.1.9/roundcubemail-1.1.9.tar.gz"
-O roundcubemail.tar.gz && \  
tar xf roundcubemail.tar.gz -C /var/www/html --strip-components 1 && \  
rm roundcubemail.tar.gz && \  
rm -rf /var/www/html/installer && \  
chown -R root:www-data /var/www/html && \  
chmod g+w /var/www/html/logs /var/www/html/temp && \  
chown -R ${APACHE_RUN_USER}:${APACHE_RUN_GROUP} /var/www/html/temp
/var/www/html/logs && \  
apt-get autoremove --purge -y $BUILD_PACKAGES && \  
rm -rf /var/lib/apt/lists/*  
  
ADD imagefiles/* /  
  
CMD ["roundcube-start.sh"]

