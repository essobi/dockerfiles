FROM php:7.1-cli  
MAINTAINER Pedro Maia <pedro.maia@ezdelivery.co>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
libxslt-dev \  
libldap2-dev \  
php-pear \  
curl \  
git \  
subversion \  
unzip \  
wget \  
&& rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-install bcmath mcrypt zip bz2 mbstring pcntl xsl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap  
  
# We dont have to limit it :)  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer \  
&& rm -rf /tmp/composer-setup.php \  
&& composer --version  
  
VOLUME [ "/data" ]  
WORKDIR [ "/data" ]  

