FROM php:7.0-apache  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libjpeg62-turbo-dev \  
libpng12-dev \  
; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache; \  
\  
apt-get clean autoclean; \  
apt-get autoremove -y; \  
rm -rf /var/lib/apt/lists/*  
  
# TODO consider removing the *-dev deps and only keeping the necessary lib*
packages  
# install Ioncube  
WORKDIR /tmp  
RUN curl -o ioncube.tar.gz
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -zxf ioncube.tar.gz \  
&& mv ioncube/ioncube_loader_lin_7.0.so /usr/local/lib/php/extensions/* \  
&& rm -Rf ioncube.tar.gz ioncube \  
&& echo "zend_extension=ioncube_loader_lin_7.0.so" >
/usr/local/etc/php/conf.d/00-ioncube-loader.ini  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN a2enmod rewrite expires  
  
CMD ["apache2-foreground"]  

