FROM ubuntu:xenial  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
locales \  
&& locale-gen en_US.UTF-8  
  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
curl \  
git \  
php-cli \  
php-curl \  
php-fpm \  
php-gd \  
php-mbstring \  
php-mcrypt \  
php-mysql \  
php-pgsql \  
php-soap \  
php-xml \  
php-zip \  
unzip \  
zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ \--filename=composer \  
&& mkdir /run/php \  
&& sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php/7.0/fpm/php-fpm.conf
\  
&& sed -i 's/\/run\/php\/php7.0-fpm.sock/0.0.0.0:9000/g'
/etc/php/7.0/fpm/pool.d/www.conf  
  
EXPOSE 9000  
  
CMD ["php-fpm7.0"]  

