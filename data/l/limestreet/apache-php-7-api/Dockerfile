FROM php:7-apache  
  
# Install git  
RUN apt-get update && apt-get install -y git subversion  
  
#Install composer  
RUN EXPECTED_SIGNATURE=$(curl https://composer.github.io/installer.sig) \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-
setup.php');") \  
&& if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ]; then rm composer-
setup.php; fi \  
&& php composer-setup.php --quiet \  
&& mv composer.phar /usr/local/bin/composer && rm composer-setup.php  
  
# Adjusting php settings  
RUN touch /usr/local/etc/php/conf.d/patryk.ini \  
&& echo "upload_max_filesize = 64M;" >> /usr/local/etc/php/conf.d/patryk.ini \  
&& echo "post_max_size = 64M;" >> /usr/local/etc/php/conf.d/patryk.ini \  
&& echo "memory_limit = 512M;" >> /usr/local/etc/php/conf.d/patryk.ini \  
&& echo "date.timezone = \"Europe/Warsaw\";" >>
/usr/local/etc/php/conf.d/patryk.ini  
  
RUN a2enmod rewrite expires  
  
VOLUME /var/www  

