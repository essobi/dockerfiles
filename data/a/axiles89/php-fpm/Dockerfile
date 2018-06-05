FROM ubuntu:latest  
MAINTAINER Dmitry Kushnerev <dkushnerev@avito.ru>  
  
ENV PHP_DIR /etc/php/7.0  
RUN apt-get update && apt-get -y install python-software-properties \  
&& apt-get -y install software-properties-common \  
&& add-apt-repository ppa:ondrej/php  
  
RUN apt-get update && apt-get -y --force-yes install \  
curl \  
php7.0-fpm \  
php7.0-amqp \  
php7.0-curl \  
php7.0-gd \  
php7.0-geoip \  
php7.0-gmp \  
php7.0-imagick \  
php7.0-intl \  
php7.0-json \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-memcached \  
php7.0-mongodb \  
php7.0-mysql \  
php7.0-opcache \  
php7.0-pgsql \  
php7.0-readline \  
php7.0-redis \  
php7.0-soap \  
php7.0-sqlite3 \  
php7.0-xml \  
php7.0-yaml \  
php7.0-zip \  
php7.0-xdebug \  
vim \  
git \  
php7.0-dev  
  
RUN git clone https://github.com/tony2001/pinba_extension /tmp/pinba_extension
\  
&& cd /tmp/pinba_extension \  
&& phpize \  
&& ./configure --enable-pinba \  
&& make install \  
&& touch $PHP_DIR/cli/conf.d/20-pinba.ini \  
&& echo 'extension=pinba.so; pinba.enabled=1' >
$PHP_DIR/cli/conf.d/20-pinba.ini \  
&& cp $PHP_DIR/cli/conf.d/20-pinba.ini $PHP_DIR/fpm/conf.d/20-pinba.ini  
  
RUN mkdir -p /var/run/php  
COPY ./etc /etc  
  
WORKDIR /var/www  
  
EXPOSE 9004  
RUN apt-get -y --force-yes install php-pear && pear channel-discover
pear.phing.info && pear install phing/phing  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
ENTRYPOINT ["/usr/sbin/php-fpm7.0", "--nodaemonize"]  
  

