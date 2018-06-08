FROM php:7-apache  
  
# Install required software  
RUN apt-get update && \  
apt-get install -y ca-certificates && update-ca-certificates && \  
apt-get install -y openssl git sudo unzip wget mysql-client libmcrypt-dev
libpng-dev libxml2-dev libcurl4-openssl-dev libcurl3 nano cron anacron  
  
## Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
RUN chmod a+x /usr/local/bin/composer  
  
# Install php extensions  
RUN pecl install mcrypt-1.0.1  
RUN docker-php-ext-enable mcrypt  
RUN docker-php-ext-install -j4 pdo_mysql gd xml zip curl intl  
  
# Install redis extension  
RUN pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable redis  
  
# Enable apache modules  
RUN a2enmod rewrite  
  
# Create projects directory  
RUN mkdir /var/www/projects  
# Add templates  
COPY templates/apache-vhost.conf /var/www/apache-vhost-template.conf  
  
# Add dummy sendmail  
COPY scripts/sendmail /usr/sbin  
RUN chmod +x /usr/sbin/sendmail  
  
# Add setup script  
COPY scripts/setup.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/setup.sh  
  
# Volumes  
VOLUME /etc/apache2/sites-available  
VOLUME /var/www  
  
# -----------------------------------------  
ENTRYPOINT ["setup.sh"]  
  
RUN chmod +x /usr/local/bin/apache2-foreground  
  
# Expose ports  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/bin/tail", "-F", "/var/log/apache2/output.log"]

