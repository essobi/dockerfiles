FROM debian:jessie  
MAINTAINER Sébastien Le Gall <seb@le-gall.net>  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
apt-utils \  
curl \  
wget \  
ca-certificates  
  
RUN apt-get update && apt-get install -y \  
zip \  
build-essential \  
acl \  
less \  
git \  
sudo  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list && \  
wget -O- https://www.dotdeb.org/dotdeb.gpg | apt-key add - && \  
apt-get update  
  
RUN apt-get install -y \  
imagemagick \  
php7.0-cli \  
php7.0-fpm \  
php7.0-dev \  
php7.0-curl \  
php7.0-gd \  
php7.0-imagick \  
php7.0-intl \  
php7.0-mcrypt \  
php7.0-sqlite \  
php7.0-xsl \  
php7.0-xdebug \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-redis \  
php7.0-xdebug  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
curl -sS https://phar.phpunit.de/phpunit.phar -k -o /usr/local/bin/phpunit &&
\  
chmod 755 /usr/local/bin/phpunit && \  
wget -q http://get.sensiolabs.org/php-cs-fixer.phar -O /usr/local/bin/php-cs-
fixer && \  
chmod a+x /usr/local/bin/php-cs-fixer  
  
RUN echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
COPY config/cli/php.ini /etc/php7.0/cli/php.ini  
COPY config/xdebug.sh /root/xdebug.sh  
RUN bash /root/xdebug.sh  
  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
RUN mkdir -p /root/.ssh  
COPY config/ssh_config /root/.ssh/config  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh && chown root:root /entrypoint.sh  
  
COPY config/fpm/php.ini /etc/php/7.0/fpm/php.ini  
COPY config/fpm/pool.d/* /etc/php/7.0/fpm/pool.d/  
  
VOLUME /srv  
WORKDIR /srv  
  
EXPOSE 9000  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/sbin/php7.0-fpm", "-F"]  
#CMD ["/usr/sbin/php7.0"]  

