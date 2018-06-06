FROM php:7.1-apache  
  
COPY config/php.ini /usr/local/etc/php/  
COPY config/vhost/* /etc/apache2/sites-available/  
  
RUN apt-get -qq update \  
&& apt-get -qq -y install bzip2 git mysql-client nano zlib1g-dev  
  
RUN apt-get -qq update \  
&& apt-get -qq install -y bzip2 git mysql-client nano re2c unzip wget  
  
RUN a2enmod rewrite \  
&& a2dissite 000-default \  
&& a2ensite zend  
  
RUN docker-php-ext-install pdo_mysql \  
&& touch /tmp/mysql.sock  
  
# Install APCU  
RUN pecl install apcu-5.1.8 \  
&& docker-php-ext-enable apcu  
  
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
  
# Install SOAP extension  
RUN docker-php-ext-install soap  
  
RUN apt-get install -y libicu-dev \  
&& docker-php-ext-install intl  
  
# Install & configure opcache  
RUN docker-php-ext-install opcache \  
&& { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=0'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# Redis  
RUN pecl install redis \  
&& docker-php-ext-enable redis  
  
# Required for PhpAmqpLib  
RUN docker-php-ext-install bcmath  
  
# amqp C / pecl extension  
RUN apt-get -qq update \  
&& apt-get -qq install -y cmake libssl-dev  
  
RUN curl -L -o /tmp/amqp.tar.gz
https://github.com/alanxz/rabbitmq-c/releases/download/v0.8.0/rabbitmq-c-0.8.0.tar.gz
\  
&& tar xfz /tmp/amqp.tar.gz \  
&& rm -r /tmp/amqp.tar.gz \  
&& mkdir -p /usr/src/php/ext \  
&& mv rabbitmq-c-0.8.0 /usr/src/php/ext/amqp \  
&& cd /usr/src/php/ext/amqp \  
&& ./configure \  
&& cmake -ENABLE_SSL_SUPPORT=ON . \  
&& cmake --build . --target install  
  
RUN pecl install amqp-1.9.3 && \  
docker-php-ext-enable amqp && \  
rm -rf /tmp/*  
  
# Required by Jose token lib  
RUN apt-get -qq install -y libgmp-dev \  
&& docker-php-ext-install gmp  
  
# Install Composer and parallel install plugin  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require hirak/prestissimo  
  

