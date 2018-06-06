FROM php:5.6-apache  
  
COPY config/php.ini /usr/local/etc/php/  
COPY config/vhost/* /etc/apache2/sites-available/  
  
RUN apt-get -qq update \  
&& apt-get -qq -y install git nano mysql-client bzip2  
  
RUN a2enmod rewrite \  
&& a2dissite 000-default \  
&& a2ensite zend  
  
RUN docker-php-ext-install pdo_mysql \  
&& touch /tmp/mysql.sock  
  
# Install APCU  
RUN pecl install apcu-4.0.11 \  
&& docker-php-ext-enable apcu  
  
# Install Gearman  
RUN apt-get install -qq -y libgearman-dev \  
&& pecl install gearman-1.1.2 \  
&& docker-php-ext-enable gearman  
  
# Install memcache | zlib1g-dev is also required for zip extension  
RUN apt-get install -qq -y zlib1g-dev \  
&& pecl install memcache-3.0.8 \  
&& docker-php-ext-enable memcache \  
&& docker-php-ext-install zip  
  
# Install memcached  
RUN apt-get install -qq -y libmemcached-dev \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached  
  
# Install amqp  
RUN apt-get install -y librabbitmq-dev \  
&& pecl install amqp-1.4.0 \  
&& docker-php-ext-enable amqp  
  
# Install solr  
RUN apt-get install -qq -y libcurl4-gnutls-dev libxml2-dev \  
&& pecl install solr \  
&& docker-php-ext-enable solr  
  
# Install gd  
RUN apt-get -qq update \  
&& apt-get install -qq -y libgd-dev libfreetype6-dev libjpeg62-turbo-dev
libpng12-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# Install bz2 extension - required for service-layer  
RUN apt-get install -qq -y libbz2-dev \  
&& docker-php-ext-install bz2  
  
# Install mcrypt - required for payment-layer  
RUN apt-get install -qq -y libmcrypt-dev \  
&& docker-php-ext-install mcrypt  
  
# Install pcntl - required for service-layer-worker  
RUN docker-php-ext-install pcntl  
  
# Install Xdebug  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
RUN echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20131226/xdebug.so' >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo 'xdebug.remote_enable=on' >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo 'xdebug.remote_connect_back=on' >>
/usr/local/etc/php/conf.d/xdebug.ini  
  
# Install SOAP extension  
RUN docker-php-ext-install soap  
  
RUN apt-get install -y libicu-dev \  
&& docker-php-ext-install intl  
  
# Install Composer and parallel install plugin  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=1.2.0 \  
&& composer global require hirak/prestissimo  

