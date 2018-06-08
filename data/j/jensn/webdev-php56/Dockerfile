FROM php:5.6-apache  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y ca-certificates && update-ca-certificates && \  
apt-get install -y openssl git sudo unzip wget mysql-client libmcrypt-dev
libpng12-dev libxml2-dev libcurl4-openssl-dev libcurl3 sendmail-bin
imagemagick cron nano  
  
# Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
RUN chmod a+x /usr/local/bin/composer  
  
RUN docker-php-ext-install -j4 pdo_mysql mcrypt gd mysql xml xmlreader zip
curl  
  
RUN a2enmod rewrite  
RUN mkdir /var/www/projects  
  
COPY templates/apache-vhost-template.conf /var/www/apache-vhost-template.conf  
  
COPY scripts/setup.sh /usr/local/bin/setup.sh  
RUN chmod +x /usr/local/bin/setup.sh  
  
VOLUME ["/etc/apache2/sites-available"]  
VOLUME ["/var/www"]  
  
ENTRYPOINT ["setup.sh"]  
RUN chmod +x /usr/local/bin/apache2-foreground  
  
EXPOSE 80  
EXPOSE 443  
CMD ["tail -f /var/log/apache2/output.log"]  

