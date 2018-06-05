FROM php:5.5-apache  
# install libs  
RUN apt-get update -y  
RUN apt-get install -y \  
ssmtp \  
ssh \  
mysql-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev  
# install extenstions  
RUN docker-php-ext-install pdo pdo_mysql mysql mbstring mcrypt xml gd  
# install xdebug  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
# change configs  
RUN echo "date.timezone = 'Australia/Sydney'" >> /usr/local/etc/php/php.ini  
RUN sed -i 's/PermitRootLogin without-password/# PermitRootLogin without-
password/' /etc/ssh/sshd_config  
RUN a2enmod rewrite  
RUN echo 'root:secret' | chpasswd  
# prepare  
WORKDIR /var/www/html  
CMD bash -c "service ssh start && source /etc/apache2/envvars && apache2
-DFOREGROUND"

