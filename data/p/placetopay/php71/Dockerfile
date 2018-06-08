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
software-properties-common \  
unzip \  
zip \  
&& add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
php7.1-cli \  
php7.1-curl \  
php7.1-fpm \  
php7.1-gd \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-pgsql \  
php7.1-soap \  
php7.1-xml \  
php7.1-zip \  
&& php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ \--filename=composer \  
&& mkdir /run/php \  
&& sed -i 's/;daemonize = yes/daemonize = no/g' /etc/php/7.1/fpm/php-fpm.conf
\  
&& sed -i 's/\/run\/php\/php7.1-fpm.sock/0.0.0.0:9000/g'
/etc/php/7.1/fpm/pool.d/www.conf \  
&& apt-get remove -y --purge software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 9000  
  
CMD ["php-fpm7.1"]  

