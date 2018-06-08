FROM drupal:8  
MAINTAINER Lodato Luciano <lodato.luciano@gmail.com>  
RUN apt-get update && apt-get install -y sqlite mysql-client wget git && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
RUN \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
ln -s /usr/local/bin/composer /usr/bin/composer && \  
composer global require drush/drush:~8  
  
RUN echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc  
  
ADD pecl-php-uploadprogress pecl-php-uploadprogress  
WORKDIR pecl-php-uploadprogress  
RUN pecl install package.xml  
RUN echo "extension=uploadprogress.so" >>
/usr/local/etc/php/conf.d/uploadprogress.ini  
RUN echo date.timezone=Europe/Rome >> /usr/local/etc/php/conf.d/timezone.ini  
  
WORKDIR /var/www/html/  

