#  
#--------------------------------------------------------------------------  
# Image Setup  
#--------------------------------------------------------------------------  
#  
# To edit the 'php-fpm' base Image, visit its repository on Github  
# https://github.com/Laradock/php-fpm  
#  
# To change its version, see the available Tags on the Docker Hub:  
# https://hub.docker.com/r/laradock/php-fpm/tags/  
#  
# Note: Base Image name format {image-tag}-{php-version}  
#  
FROM php:7.1-fpm  
  
COPY . /bd_build  
ADD ./bin /usr/sbin  
  
#  
#--------------------------------------------------------------------------  
# Core Software's Installation  
#--------------------------------------------------------------------------  
#  
RUN apt-get update -yqq  
RUN apt-get install -y --no-install-recommends \  
autoconf \  
curl \  
g++ \  
libfreetype6-dev \  
libgmp-dev \  
libicu-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng12-dev \  
libpq-dev \  
librabbitmq-dev \  
libssl-dev \  
libxml2-dev \  
libz-dev \  
wget \  
zlib1g-dev \  
# --  
libzip-dev \  
zip \  
unzip \  
python-setuptools  
  
  
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key
add -  
RUN apt-get update -yqq && \  
apt-get install -y lsb-release  
### <include> ../inc/image-optimizers  
#  
#--------------------------------------------------------------------------  
# PHP Installation  
#--------------------------------------------------------------------------  
#  
RUN docker-php-ext-install bcmath  
RUN docker-php-ext-install exif  
RUN docker-php-ext-install gmp  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install opcache  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install pdo_pgsql  
RUN docker-php-ext-install pgsql  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install tokenizer  
RUN docker-php-ext-install xml  
RUN docker-php-ext-install zip  
  
RUN pecl update-channel  
RUN pecl install -o -f redis && docker-php-ext-enable redis  
RUN pecl install -o -f xdebug && docker-php-ext-enable xdebug  
RUN pecl install -o -f swoole && docker-php-ext-enable swoole  
RUN pecl install -o -f amqp && docker-php-ext-enable amqp  
# RUN pecl install -o -f mongodb && docker-php-ext-enable mongodb  
RUN pecl install -o -f memcached && docker-php-ext-enable memcached  
  
# imagemagick  
RUN apt-get install -y libmagickwand-dev imagemagick  
RUN pecl install -o -f imagick && docker-php-ext-enable imagick  
  
#####################################  
# Human Language and Character Encoding Support:  
#####################################  
RUN docker-php-ext-configure intl && \  
docker-php-ext-install intl  
  
#####################################  
# LDAP:  
#####################################  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
  
# Stop xDebug  
RUN sed -i 's/^zend_extension=/;zend_extension=/g'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
ADD ./conf.d/*.ini /usr/local/etc/php/conf.d/  
ADD ./php-fpm.d/*.conf /usr/local/etc/php-fpm.d/  
  
#  
#--------------------------------------------------------------------------  
# Postgres client  
#--------------------------------------------------------------------------  
#  
# USER root  
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key
add -  
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release
-cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'  
RUN apt-get update -yq && \  
apt-get install -y postgresql-client  
  
RUN curl -s http://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
#  
#--------------------------------------------------------------------------  
# Clear code  
#--------------------------------------------------------------------------  
#  
RUN apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* /var/tmp/* /tmp/pear \  
&& mkdir -p /var/www  
  
WORKDIR /var/www  
  
CMD ["php-fpm"]  
  
EXPOSE 9000  

