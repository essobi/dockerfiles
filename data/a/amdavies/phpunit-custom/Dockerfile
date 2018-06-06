# PHPUnit Docker Container. With customisations for WPS  
FROM composer/composer:php7  
MAINTAINER Alex Davies  
  
# Run some Debian packages installation.  
ENV PACKAGES="php-pear curl libxml2-dev bzip2 libfreetype6 libfontconfig"  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends $PACKAGES && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Node.js v6  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
# Install phantomjs  
RUN npm -g install phantomjs-prebuilt  
  
# Run xdebug installation.  
RUN curl -L http://pecl.php.net/get/xdebug-2.4.0.tgz >>
/usr/src/php/ext/xdebug.tgz && \  
tar -xf /usr/src/php/ext/xdebug.tgz -C /usr/src/php/ext/ && \  
rm /usr/src/php/ext/xdebug.tgz && \  
docker-php-ext-install xdebug-2.4.0 && \  
docker-php-ext-install pcntl && \  
php -m  
  
# Goto temporary directory.  
WORKDIR /tmp  
  
# Run composer and phpunit installation.  
RUN composer selfupdate && \  
composer require "phpunit/phpunit:~5.4.2" \--prefer-source --no-interaction &&
\  
ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit  
  
# Set up the application directory.  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set up the command arguments.  
ENTRYPOINT ["/usr/local/bin/phpunit"]  
CMD ["--help"]  
  
# Configure PHP Extensions  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install soap  
  
# Suppress errors and other interesting bits within php ini  
COPY conf/php.ini /usr/local/etc/php/php.ini  

