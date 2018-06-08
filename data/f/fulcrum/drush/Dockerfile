FROM fulcrum/php:latest-alpine  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
  
RUN apk add --no-cache --virtual containerbuild git php5-phar && \  
apk add --no-cache curl curl-dev mysql-client php5-openssl && \  
cd /usr/local && \  
curl -sS https://getcomposer.org/installer | php && \  
/bin/mv composer.phar bin/composer && \  
deluser php && \  
adduser -h /tmp/phphome -s /bin/sh -D -H -u 1971 php && \  
mkdir -p /usr/share/drush/commands/ /tmp/phphome drush8 && \  
chown php.php /tmp/phphome drush8 && \  
su - php -c "cd /usr/local/drush8 && composer require drush/drush:8.*" && \  
ln -s /usr/local/drush8/vendor/drush/drush/drush /usr/local/bin/drush && \  
su - php -c "/usr/local/bin/drush @none dl registry_rebuild-7.x" && \  
mv /tmp/phphome/.drush/registry_rebuild /usr/share/drush/commands/ && \  
deluser php && \  
adduser -h /var/www/html -s /bin/sh -D -H -u 1971 php && \  
apk del containerbuild && \  
rm /usr/local/bin/composer  
  
USER php  
  
# Move to the directory were the php files stands  
WORKDIR /var/www/html  
  
ENTRYPOINT ["/usr/local/bin/drush"]

