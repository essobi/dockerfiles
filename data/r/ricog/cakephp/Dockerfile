FROM ricog/php-fpm:php7  
MAINTAINER Rick Guyer <ricoguyer@gmail.com>  
  
# Install required server packages  
#  
# curl - CakePHP ??  
# git - To install from a remote git repo  
# php5-cli - CakePHP 2 and 3  
# php5-intl - CakePHP 3  
# php5-readline - CakePHP 3 - required by boris shell  
# php5-sqlite - CakePHP 3 - required by debugkit  
# php5-xsl - CakePHP 2  
#  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
php-cli \  
php-intl \  
php-readline \  
php-sqlite3 \  
php-xsl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN sed -i '/upload_max_filesize /c upload_max_filesize = 20M'
/etc/php/7.0/fpm/php.ini  
RUN sed -i '/post_max_size /c post_max_size = 20M' /etc/php/7.0/fpm/php.ini  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
RUN usermod -u 1000 www-data  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm7.0"]  

