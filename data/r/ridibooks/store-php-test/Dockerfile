FROM php:7.1  
LABEL maintainer="Heechan Yang <heechan@ridi.com>"  
  
RUN apt-get update && apt-get install -yqq \  
git \  
libmcrypt-dev \  
python3 \  
python3-pip \  
unzip \  
zlib1g-dev  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/bin/composer  
  
RUN docker-php-ext-install bcmath pdo_mysql mcrypt zip  
RUN pecl install apcu xdebug && docker-php-ext-enable apcu xdebug  
RUN pip3 install awscli --upgrade  

