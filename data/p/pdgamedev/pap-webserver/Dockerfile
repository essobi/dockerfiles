FROM php:7.1-apache  
  
ENV REFRESHED_AT 24-04-2017  
RUN apt-get update && apt-get install -y \  
git \  
apt-transport-https \  
vim \  
telnet \  
cron \  
zlib1g-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmemcached-dev \  
libz-dev \  
libapache2-mod-rpaf \  
libmagickwand-dev \  
libmcrypt-dev \  
libxml2 \  
libxml2-dev \  
libpng12-dev \  
libicu-dev \  
php-pear \  
pkg-config \  
python-pip \  
make \  
openssl \  
libssl-dev \  
libcurl4-openssl-dev  
  
RUN pip install supervisor \  
&& pecl install mongodb xdebug imagick memcached \  
&& docker-php-ext-enable imagick memcached \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install xml opcache zip mysqli pdo pdo_mysql gd intl mcrypt
bcmath sockets pcntl \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN echo "extension=mongodb.so" > $PHP_INI_DIR/conf.d/mongodb.ini  
  
# Add users, add root rights, add alias for phpunit  
RUN adduser devel --home /home/devel --uid 1000 \  
\--shell /bin/bash \  
\--disabled-password \  
\--gecos "" && \  
echo "devel ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
echo "alias phpunit='php /var/www/vendor/bin/phpunit'" >> /home/devel/.bashrc  
  
# apache2  
COPY conf/apache2.conf /etc/apache2/apache2.conf  
COPY conf/ports.conf /etc/apache2/ports.conf  
COPY conf/rpaf.conf /etc/apache2/mods-enabled/rpaf.conf  
# enable rewrite  
RUN a2enmod rewrite && a2enmod rpaf  
  
# php.ini  
COPY conf/php.ini /usr/local/etc/php/conf.d/php.ini  
  
# Make port 8080 accessible  
EXPOSE 8080  
# Set environment variables  
ENV APACHE_RUN_USER devel  
ENV APACHE_RUN_GROUP staff  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV LANG C  
  
# Some cleanup  
RUN apt-get -q autoremove &&\  
apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin  
  
# Starting directory  
WORKDIR /var/www

