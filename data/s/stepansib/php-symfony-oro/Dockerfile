FROM php:7.2-fpm  
MAINTAINER Stepan Yudin <stepan.sib@gmail.com>  
  
ENV REFRESHED_AT 2018–05-30  
# Install libs  
RUN apt-get update && apt-get install -y \  
zlib1g-dev \  
libicu-dev g++ \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
libldap2-dev \  
libxml2-dev \  
libcurl4-openssl-dev \  
libtidy-dev \  
zip \  
unzip \  
wget \  
xvfb \  
wkhtmltopdf \  
mysql-client \  
git \  
mc \  
ruby-full \  
gnupg  
  
# Install fresh node & npm  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs \  
build-essential  
  
# Configure PHP extensions  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-configure pcntl  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ --with-png-dir=/usr/include/  
  
# Install PHP extensions  
RUN docker-php-ext-install \  
curl \  
intl \  
pcntl \  
gd \  
ldap \  
opcache \  
pdo \  
pdo_mysql \  
soap \  
zip \  
tidy \  
bcmath  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Symfony installer  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony  
RUN chmod a+x /usr/local/bin/symfony  
  
# Install PHPUnit  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
  
# Install Codeception  
RUN curl -LsS http://codeception.com/php5/codecept.phar -o
/usr/local/bin/codecept  
RUN chmod a+x /usr/local/bin/codecept  
  
# Create Codeception alias  
#RUN echo 'alias codecept="./vendor/codeception/codeception/codecept"' >>
~/.bashrc  
#RUN . ~/.bashrc  
# Install XDebug  
#RUN pecl install xdebug  
#RUN docker-php-ext-enable xdebug  
# Install PHPStan  
RUN composer global require phpstan/phpstan ^0.9 --prefer-dist  
  
# Install PHP Code Sniffer  
RUN composer global require squizlabs/php_codesniffer --prefer-dist  
  
# Install PHP MEss Detector  
RUN composer global require phpmd/phpmd --prefer-dist  
  
# Disable XDebug  
#RUN echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
# && echo "xdebug.remote_enable=0" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
# && echo "xdebug.remote_autostart=0" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
# && echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
# && echo "xdebug.idekey=PHPSTORM" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
# && echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
# Install Bundler & configure Ruby gems install command  
RUN gem install bundler  
#RUN echo -e "---\ninstall: --user-install" > ~/.gemrc  
# Configure PHP and FPM  
COPY ./php.ini /usr/local/etc/php/  
COPY php-fpm.conf /etc/php-fpm.conf  
RUN sed -i 's/listen = 127.0.0.1:9000/listen = 9000/' /usr/local/etc/php-
fpm.d/www.conf  

