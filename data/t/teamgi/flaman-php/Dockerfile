FROM php:5.6.30-apache  
  
# Generate SSL cert  
RUN cd /tmp \  
&& openssl genrsa -des3 -passout pass:x -out snakeoil.pass.key 2048 \  
&& openssl rsa -passin pass:x -in snakeoil.pass.key -out snakeoil.key \  
&& openssl req -new -subj "/C=US/ST=California/L=San
Francisco/O=Dis/CN=localhost" -key snakeoil.key -out snakeoil.csr \  
&& openssl x509 -req -days 3650 -in snakeoil.csr -signkey snakeoil.key -out
snakeoil.pem \  
&& mv ./snakeoil.key /etc/ssl/private/ssl-cert-snakeoil.key \  
&& mv ./snakeoil.pem /etc/ssl/certs/ssl-cert-snakeoil.pem \  
&& rm -rf /tmp/*  
  
#Enable SSL and other stuff  
RUN a2enmod actions ssl rewrite headers  
  
# Install our magento php extension deps  
RUN buildDeps=" \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir \  
&& docker-php-ext-install \  
gd \  
mbstring \  
mysqli \  
mcrypt \  
mysql \  
pdo_mysql \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN sed -i '1 a xdebug.remote_autostart=true'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_connect_back=Off'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_port=9000' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN sed -i '1 a xdebug.idekey=PHPSTORM' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN sed -i '1 a xdebug.remote_host=docker_host'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
# NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install -y nodejs build-essential \  
&& npm install -g parallelshell  
  
RUN apt-get install -y git  
  
RUN apt-get -yq update && \  
apt-get -yqq install ssh

