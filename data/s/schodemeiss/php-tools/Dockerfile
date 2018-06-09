FROM php:7.2-cli  
MAINTAINER Andrew Barlow <andrew.barlow@gmail.com>  
  
# Grab the requirements of Composer  
RUN apt-get update \  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libgmp-dev \  
libbz2-dev \  
libxslt-dev \  
libldap2-dev \  
curl \  
git \  
subversion \  
unzip \  
wget \  
&& apt-get clean \  
&& apt-get autoremove\  
&& rm -r /var/lib/apt/lists/*  
  
# Install some common PHP extensions  
RUN docker-php-ext-install bcmath gmp zip bz2 mbstring pcntl xsl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap  
  
# Add our PHP settings file  
ADD php-tools.ini /usr/local/etc/php/conf.d/php-tools.ini  
  
# Add our tools dependencies  
ADD composer.json /composer/composer.json  
  
# Programatically install composer, including signature check  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer && rm -rf /tmp/composer-setup.php  
  
# Register the COMPOSER_HOME environment variable  
ENV COMPOSER_HOME /composer  
  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH /composer/vendor/bin:$PATH  
  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# Ensure composer never asks questions  
ENV COMPOSER_NO_INTERACTION 1  
# Install our tools and then clear the cache  
RUN composer install -v --no-ansi --no-progress --no-dev --no-suggest -d
$COMPOSER_HOME \  
&& composer clear-cache  
  
# Set up the working directory  
WORKDIR /app  
  
# Default action is to run PHP interactively  
CMD ["php" , "-a"]  

