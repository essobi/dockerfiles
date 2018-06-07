FROM jedisct1/phusion-baseimage-latest:16.04  
MAINTAINER gimatov@gmail.com  
  
ARG PHP_VERSION  
ENV PHP_VERSION ${PHP_VERSION:-7.2}  
ARG XDEBUG_PORT  
ENV XDEBUG_PORT ${XDEBUG_PORT:-9001}  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# DNS update: to run apt-get and to let the docker build process access the
internet.  
#RUN "sh" "-c" "echo nameserver 8.8.8.8 >> /etc/resolv.conf"  
# https://docs.docker.com/engine/faq/  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -y update \  
&& apt-get install -y software-properties-common python-software-properties  
  
RUN apt-get install -y language-pack-en-base  
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php \  
&& apt-get -y update  
  
# php-fpm have to be installed at the base image  
# child image installation gets "memcached module required" error  
RUN apt-get install -y php${PHP_VERSION} php-pear php${PHP_VERSION}-dev
php${PHP_VERSION}-cli php${PHP_VERSION}-fpm php${PHP_VERSION}-curl
php${PHP_VERSION}-gd php${PHP_VERSION}-gmp  
RUN apt-get install -y php${PHP_VERSION}-apcu php${PHP_VERSION}-mysqlnd
php${PHP_VERSION}-sqlite3 php${PHP_VERSION}-memcached
php${PHP_VERSION}-memcache php${PHP_VERSION}-xdebug  
RUN apt-get install -y php${PHP_VERSION}-imagick php${PHP_VERSION}-imap
php${PHP_VERSION}-bcmath php${PHP_VERSION}-xml php${PHP_VERSION}-mbstring
php${PHP_VERSION}-zip  
  
RUN apt-get install -y imagemagick sqlite3 unzip  
RUN apt-get install -y mysql-client  
  
# Redis  
RUN curl -L -o phpredis.zip
https://github.com/phpredis/phpredis/archive/develop.zip \  
&& unzip -q phpredis.zip \  
&& rm phpredis.zip \  
&& cd phpredis-* \  
&& phpize \  
&& ./configure \  
&& make && make install \  
&& cd ../ \  
&& rm -r phpredis-* \  
&& cat > /etc/php/${PHP_VERSION}/mods-available/redis.ini \  
&& echo 'extension=redis.so' > /etc/php/${PHP_VERSION}/mods-
available/redis.ini \  
&& phpenmod redis  
  
# Node  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
# && apt-get install -y npm  
# Pinba  
RUN git clone https://github.com/tony2001/pinba_extension.git \  
&& cd pinba_extension \  
&& phpize \  
&& ./configure --enable-pinba \  
&& make && make install \  
&& cd ../ \  
&& rm -r pinba_extension \  
&& cat > /etc/php/${PHP_VERSION}/mods-available/pinba.ini \  
&& echo "extension=pinba.so\npinba.enabled=1\npinba.server=pinba:30002" >
/etc/php/${PHP_VERSION}/mods-available/pinba.ini \  
&& phpenmod pinba  
  
# Rotator  
RUN git clone https://bitbucket.org/magicpro/rotator \  
&& cd rotator/rotator_7.0 \  
&& phpize \  
&& ./configure \  
&& make && make install \  
&& cd ../../ \  
&& rm -r rotator \  
&& cat > /etc/php/${PHP_VERSION}/mods-available/rotator.ini \  
&& echo "extension=rotator.so" > /etc/php/${PHP_VERSION}/mods-
available/rotator.ini \  
&& phpenmod rotator  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
# Config files  
COPY conf/xdebug.ini /etc/php/${PHP_VERSION}/mods-available/xdebug.ini  
COPY conf/opcache.ini /etc/php/${PHP_VERSION}/mods-available/opcache.ini  
COPY conf/apcu.ini /etc/php/${PHP_VERSION}/mods-available/apcu.ini  
COPY conf/memcached.ini /etc/php/${PHP_VERSION}/mods-available/memcached.ini  
COPY conf/php-cli.ini /etc/php/${PHP_VERSION}/cli/php.ini  
COPY conf/php.ini /etc/php/${PHP_VERSION}/fpm/php.ini  
COPY conf/php.ini /etc/php/${PHP_VERSION}/php.ini  

