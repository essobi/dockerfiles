FROM csanchez/jenkins-swarm-slave:1.22  
MAINTAINER Pavel Gopanenko <pgopanenko@gmail.com>  
  
USER root  
  
RUN echo "deb http://ftp.ru.debian.org/debian/ squeeze main" >
/etc/apt/sources.list.d/squeeze.list  
  
COPY preferences /etc/apt/preferences.d/preferences  
  
RUN apt-get update && apt-get install -y \  
php5 \  
php5-common \  
php5-mcrypt \  
php5-curl \  
php5-cli \  
php5-mysql \  
php5-sqlite \  
php5-xdebug \  
php5-dev \  
php-pear \  
libpcre3-dev \  
mercurial git make gcc  
  
RUN pecl install apc  
RUN echo "extension=apc.so" > /etc/php5/cli/conf.d/apc.ini  
  
COPY suhosin.ini /etc/php5/cli/conf.d/suhosin.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/tmp &&
/bin/mv -f /tmp/composer.phar /usr/local/bin/composer  

