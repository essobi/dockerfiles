FROM tetraweb/php:7.0  
  
# Update and Install Packages  
RUN apt-get update -y && apt-get install -y \  
unzip \  
libfontconfig \  
php5-intl \  
jq  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"

