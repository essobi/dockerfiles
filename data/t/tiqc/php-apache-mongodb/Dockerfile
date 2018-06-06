FROM navysu/php-apache-ssmtp  
  
MAINTAINER Haijun (Navy) Su <navysu@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends
libcurl4-openssl-dev pkg-config libssl-dev unzip libzip-dev && rm -r
/var/lib/apt/lists/*  
  
RUN mkdir -p /storage/wwwroot \  
&& pecl install mongodb \  
&& pecl install zip \  
&& docker-php-ext-enable mongodb \  
&& docker-php-ext-enable zip  
  
RUN cd /storage/wwwroot && php -r "copy('https://getcomposer.org/installer',
'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& php composer.phar require mongodb/mongodb \  
&& rm composer.phar  
  
WORKDIR /var/www/html  
  
EXPOSE 80  

