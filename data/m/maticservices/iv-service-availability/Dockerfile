FROM php:7.1-apache  
  
RUN \  
apt-get update -qq \  
&& apt-get install -qq -y \  
software-properties-common \  
build-essential \  
librabbitmq-dev \  
libmcrypt-dev \  
libpng12-dev \  
libssl-dev \  
openssl \  
wget \  
git \  
unzip \  
cron \  
vim \  
supervisor \  
#supervisord  
&& mkdir -p /var/log/supervisor \  
# mongodb  
&& pecl install mongodb \  
&& docker-php-ext-enable mongodb \  
# amqp  
&& pecl install amqp \  
&& docker-php-ext-enable amqp \  
# xdebug  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
# composer  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer \  
# cleanup  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get remove -y build-essential \  
&& apt-get autoremove -y \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-install \  
zip\  
pdo \  
pcntl \  
mcrypt \  
pdo_mysql\  
gd  
  
COPY php.ini /usr/local/etc/php/php.ini  
COPY default.conf /etc/apache2/sites-enabled/000-default.conf  
COPY supervisord/supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN ln -s /app /var/www/site  
RUN a2enmod headers rewrite  
  
CMD ["/usr/bin/supervisord", "-n"]  

