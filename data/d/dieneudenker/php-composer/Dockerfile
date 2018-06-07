FROM php:7.1.11-cli-jessie  
  
# Install system dependencies  
RUN apt-get update  
RUN apt-get -qq install libpng-dev git  
  
# Install PHP Libraries  
RUN docker-php-ext-install gd zip  
  
# Install Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Define working directory.  
WORKDIR /app

