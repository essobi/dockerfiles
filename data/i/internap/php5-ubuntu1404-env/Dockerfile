FROM ubuntu:14.04  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git
curl maven php5-curl php5-cli php5-mcrypt \  
php5-xdebug php5-mysql memcached php5-memcached php5-sqlite php5-gd php5-dev
php5-intl php5-json libsqlite3-dev \  
libmysqlclient-dev  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN pecl install runkit  
RUN echo "extension=runkit.so" >> /etc/php5/cli/php.ini  
  
RUN php5enmod mcrypt  
  
RUN mkdir -p /opt/project  
VOLUME /opt/project  
WORKDIR /opt/project  

