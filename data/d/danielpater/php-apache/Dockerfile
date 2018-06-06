FROM php:7.0-apache  
  
# Remove Apache Server Signature  
RUN { \  
echo 'ServerTokens ProductOnly'; \  
echo 'ServerSignature Off'; \  
} >> /etc/apache2/apache2.conf  
  
  
# install the PHP extensions we need  
RUN apt-get update \  
#apt-get install -y libpng12-dev libjpeg-dev && rm -rf /var/lib/apt/lists/* \  
&& apt-get install -y libssl-dev libcurl4-openssl-dev pkg-config libxml2-dev
libmcrypt-dev libjpeg-dev libpng-dev zlib1g-dev libicu-dev g++  
  
RUN docker-php-ext-install mysqli opcache pdo_mysql mcrypt bcmath ctype curl
dom gd intl mbstring hash simplexml soap xml zip json iconv  
#RUN docker-php-ext-install spl  
  
# set PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
#RUN { \  
# echo 'opcache.memory_consumption=128'; \  
# echo 'opcache.interned_strings_buffer=8'; \  
# echo 'opcache.max_accelerated_files=4000'; \  
# echo 'opcache.revalidate_freq=2'; \  
# echo 'opcache.fast_shutdown=1'; \  
# echo 'opcache.enable_cli=1'; \  
# echo 'date.timezone = "Europe/Berlin"'; \  
# } > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN a2enmod rewrite expires  
  
# Do not send HTTP-Header with PHP Version  
# Higher upload limit for importing WP Backups for example  
# ADD CUSTOM PHP.INI SETTINGS HERE  
RUN { \  
echo 'memory_limit = 128M'; \  
echo 'max_input_vars = 3000'; \  
echo 'expose_php = Off'; \  
echo 'upload_max_filesize = 200M'; \  
echo 'post_max_size = 201M'; \  
} > /usr/local/etc/php/php.ini  
  
# For SFTP access to work in docker-compose setup with SFTP  
RUN chmod -R o+w /var/www/html  
  
CMD ["apache2-foreground"]  

