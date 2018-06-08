FROM php:5.6-apache  
MAINTAINER aspirationhub  
COPY .htaccess /home  
COPY docker-entrypoint.sh /home  
ENV WORDPRESS_DB=wordpress WORDPRESS_URL=http://localhost
WORDPRESS_ADMIN_USER=root WORDPRESS_ADMIN_PASS=root
WORDPRESS_ADMIN_EMAIL=example@example.com  
ENV APACHE_RUN_USER=www-data APACHE_RUN_GROUP=www-data
APACHE_LOG_DIR=/var/log/apache2 APACHE_PID_FILE=/var/run/apache2.pid
APACHE_RUN_DIR=/var/run/apache2 APACHE_LOCK_DIR=/var/lock/apache2  
RUN apt-get update && apt-get install mysql-client -y && mkdir -p
$APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR && docker-php-ext-install
mysql && \  
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && mv wp-cli.phar /usr/local/bin/wp && chmod +x
/home/docker-entrypoint.sh && a2enmod rewrite  
VOLUME /var/www/html  
EXPOSE 80  
CMD /home/docker-entrypoint.sh  

