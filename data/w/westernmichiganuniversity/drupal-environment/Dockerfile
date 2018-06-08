FROM alpine:3.4  
# Install Apache, PHP, extensions and related tools.  
RUN apk --no-cache add \  
ca-certificates \  
curl \  
gzip \  
php5-apache2 \  
php5-cli \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-exif \  
php5-ftp \  
php5-gd \  
php5-json \  
php5-ldap \  
php5-mcrypt \  
php5-openssl \  
php5-pdo_mysql \  
php5-phar \  
php5-posix \  
php5-pspell \  
php5-sockets \  
php5-xml \  
php5-zip \  
php5-zlib \  
tar \  
wget \  
zip  
  
# Install MariaDB server and client.  
RUN apk --no-cache add mariadb mariadb-client  
  
# Configure Apache.  
EXPOSE 80  
RUN mkdir -p /run/apache2  
RUN mkdir -p /var/www/html  
ADD conf/apache.conf /etc/apache2/conf.d/docker-drupal-environment.conf  
  
# Configure MariaDB.  
RUN mysql_install_db --user=mysql \  
&& mkdir -p /run/mysqld \  
&& chown mysql:mysql /run/mysqld  
ADD conf/my.cnf /etc/mysql/my.cnf  
ADD conf/mysql-secure.sql /docker-drupal-environment-mysql-secure.sql  
RUN mysqld --user=mysql --bootstrap < /docker-drupal-environment-mysql-
secure.sql  
  
# Copy in our entrypoint script.  
COPY bin/docker-drupal-environment-* /usr/local/bin/  
  
WORKDIR /var/www/html  
ENTRYPOINT ["docker-drupal-environment-entrypoint.sh"]  
CMD ["php", "-a"]  

