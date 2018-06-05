FROM php:7.2-apache-stretch  
  
COPY . /var/www/html  
COPY ./vhost.conf /etc/apache2/sites-available/000-default.conf  
COPY ./start.sh /usr/local/bin/start  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer \  
| php -- --install-dir=/usr/local/bin \  
&& mv /usr/local/bin/composer.phar /usr/local/bin/composer  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
git \  
libssl-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
libpq-dev  
RUN docker-php-ext-install mbstring tokenizer pcntl pdo pdo_mysql bcmath \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd zip ctype json soap  
  
# Install node  
RUN apt install -y software-properties-common gnupg && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs && \  
apt-get install -y build-essential  
  
# Install pecl extensions  
RUN pecl install mongodb \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug mongodb  
  
RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.port_remot=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_autostart=1" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.idekey=docker" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini  
  
RUN chown -R www-data:www-data /var/www/html \  
&& chmod u+x /usr/local/bin/start \  
&& a2enmod rewrite headers  
  
CMD ["/usr/local/bin/start"]

