FROM internetrix/webdev:lap  
MAINTAINER Jason Zhang <jason.zhang@internetrix.com.au>  
ARG DEBIAN_FRONTEND=noninteractive  
  
### PHP Configuration  
# Install xdebug for PHP 5.6+  
RUN apt-get install php-xdebug  
  
# Add custom PHP 5.6 and 7.0 config  
ADD config/php/webdev_common_php_config.ini
/etc/php/webdev_common_php_config.ini  
RUN cat /etc/php/webdev_common_php_config.ini | tee -a
/etc/php/5.6/fpm/php.ini /etc/php/7.0/fpm/php.ini  
  
# Specific config for php 5.6  
#RUN sed -i -e 's~xdebug.remote_port=[0-9]*~xdebug.remote_port=9056~g'
/etc/php/5.6/fpm/php.ini  
# Specific config for php 7.0  
#RUN sed -i -e 's~xdebug.remote_port=[0-9]*~xdebug.remote_port=9070~g'
/etc/php/7.0/fpm/php.ini  
### Apache Configuration  
RUN a2enmod rewrite proxy proxy_fcgi proxy_http expires ssl vhost_alias
headers env  
  
# Setup Apache config for webdev server  
ADD config/apache/conf/webdev.conf /etc/apache2/conf-available/webdev.conf  
RUN a2enconf webdev.conf  
  
# Setup /phpinfo alias  
RUN mkdir /var/www/php/ && \  
chmod +x /var/www/php/ && \  
echo '<?php phpinfo() ?>' > /var/www/php/phpinfo.php && \  
chmod +x /var/www/php/phpinfo.php && \  
echo 'Alias /phpinfo /var/www/php/phpinfo.php' > /etc/apache2/conf-
available/phpinfo.conf && \  
a2enconf phpinfo.conf  
  
# Setup script to handle project sync to /tmpwww/ folder  
ADD rsync_project_to_tmpwww.php /var/www/php/rsync_project_to_tmpwww.php  
RUN chmod +x /var/www/php/rsync_project_to_tmpwww.php  
  
# Setup Apache wildcard vhost for multi PHP versions  
ADD config/apache/sites/apache-wildcard-php70-vhost.conf /etc/apache2/sites-
available/001-wildcard-php70-vhost.conf  
ADD config/apache/sites/apache-wildcard-php56-vhost.conf /etc/apache2/sites-
available/002-wildcard-php56-vhost.conf  
  
# Setup Apache wildcard vhost for multi PHP versions  
ADD config/apache/sites/apache-wildcard-tmpfs-php70-vhost.conf
/etc/apache2/sites-available/003-wildcard-tmpfs-php70-vhost.conf  
  
# Old PHP versions. 53, 54, 55  
ADD config/apache/sites/apache-wildcard-php53-vhost.conf /etc/apache2/sites-
available/004-wildcard-php53-vhost.conf  
ADD config/apache/sites/apache-wildcard-php54-vhost.conf /etc/apache2/sites-
available/005-wildcard-php54-vhost.conf  
ADD config/apache/sites/apache-wildcard-php55-vhost.conf /etc/apache2/sites-
available/006-wildcard-php55-vhost.conf  
  
# Default wildcard has lowest priority  
ADD config/apache/sites/apache-wildcard-default-vhost.conf /etc/apache2/sites-
available/111-wildcard-default.conf  
  
RUN a2ensite 001-wildcard-php70-vhost.conf 002-wildcard-php56-vhost.conf
003-wildcard-tmpfs-php70-vhost.conf 111-wildcard-default.conf \  
004-wildcard-php53-vhost.conf 005-wildcard-php54-vhost.conf 006-wildcard-
php55-vhost.conf  
  
## Old php version fpm pools  
ADD config/php/fpm/php53-fpm-www.conf /etc/php53/fpm/pool.d/www.conf  
ADD config/php/fpm/php54-fpm-www.conf /etc/php54/fpm/pool.d/www.conf  
ADD config/php/fpm/php55-fpm-www.conf /etc/php55/fpm/pool.d/www.conf  
  
# Setup Webgrind - web based front-end xdebug profile information presentation
tool  
ADD config/apache/conf/apache-phpwebgrind.conf /etc/apache2/conf-
available/phpwebgrind.conf  
RUN mkdir /var/www/php/xdebug.profiler && \  
chmod 777 /var/www/php/xdebug.profiler && \  
cd /var/www/php && \  
git clone https://github.com/jokkedk/webgrind.git webgrind && \  
a2enconf phpwebgrind.conf  
  
# Forward apache logs to docker console.  
RUN ln -sf /dev/stdout /var/log/apache2/access.log  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
# Run apache in foreground  
ADD apache-foreground.sh /usr/local/bin/  
RUN ["chmod", "+x", "/usr/local/bin/apache-foreground.sh"]  
  
EXPOSE 80 443  
ENV WEBDEV_PHPMYADMIN_DB_HOST mariadb  
ENV WEBDEV_PHPMYADMIN_DB_USER root  
ENV WEBDEV_PHPMYADMIN_DB_PW root123  
ENV WEBDEV_ENABLE_PHP_53_FPM 0  
ENV WEBDEV_ENABLE_PHP_54_FPM 0  
ENV WEBDEV_ENABLE_PHP_55_FPM 0  
ENV WEBDEV_ENABLE_PHP_56_FPM 1  
ENV WEBDEV_ENABLE_PHP_70_FPM 1  
ENV WEBDEV_REMOTE_HOST_IP 192.168.99.1  
ENV WEBDEV_CIFS_HOST_FOLDER //192.168.99.1/www  
ENV WEBDEV_CIFS_USER container  
ENV WEBDEV_CIFS_PW container123  
ENV WEBDEV_POSTFIX_RELAYHOST [mailhog]:1025  
CMD ["/usr/local/bin/apache-foreground.sh"]

