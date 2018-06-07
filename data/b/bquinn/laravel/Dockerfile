FROM php:5.6-apache  
  
# Based on ganiutomo  
# https://github.com/ganiutomo/docker-php-
laravel/blob/master/5.6/apache/Dockerfile  
  
RUN apt-get update && apt-get install -y \  
nano \  
freetds-dev \  
freetds-bin \  
libicu-dev \  
libpq-dev \  
libmcrypt-dev \  
libldap2-dev \  
libjpeg-dev \  
libpng12-dev \  
git \  
libnotify-bin \  
supervisor \  
&& rm -r /var/lib/apt/lists/* \  
&& cp -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/ \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/ \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install \  
gd \  
intl \  
mbstring \  
mcrypt \  
pcntl \  
pdo_dblib \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
zip \  
opcache  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Get LDAP enabled  
RUN ln -fs /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/ \  
&& docker-php-ext-install ldap \  
&& a2enmod rewrite ldap headers  
  
# Install nodejs-legacy and npm  
RUN apt-get update && apt-get install -y nodejs-legacy npm \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get upgrade -y nodejs \  
&& npm update -g npm \  
&& npm install -g bower gulp jscs jshint typescript typings \  
&& npm rebuild node-sass --no-bin-links  
  
# Install PHP xdebug  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
  
COPY config/apache2.conf /etc/apache2/apache2.conf  
COPY config/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
COPY config/freetds/freetds.conf /etc/freetds/  
COPY config/freetds/locales.conf /etc/freetds/  
  
WORKDIR /var/www/laravel  
  
Expose 80 443  
# Toss our composer includes into the PATH (for phpunit)  
ENV PATH /var/www/laravel/vendor/bin:$PATH  
  
# Add Apache log location to environment  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV TERM xterm  
  
CMD ["apache2", "-DFOREGROUND"]  

