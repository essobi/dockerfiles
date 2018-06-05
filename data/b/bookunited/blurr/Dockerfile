FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get install -y locales \  
&& locale-gen en_US en_US.UTF-8 \  
nl_NL nl_NL.UTF-8 \  
de_DE de_DE.UTF-8 \  
fr_FR fr_FR.UTF-8 \  
es_ES es_ES.UTF-8 \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  
  
RUN apt-get update \  
&& apt-get install -y nginx curl zip unzip git software-properties-common
supervisor \  
&& add-apt-repository -y ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y \  
php7.2-fpm \  
php7.2-cli \  
php7.2-common \  
php7.2-mbstring \  
php7.2-mysql \  
php7.2-sqlite \  
php7.2-xml \  
php7.2-curl \  
php7.2-soap \  
php7.2-xdebug \  
&& php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ \--filename=composer \  
&& mkdir /run/php \  
&& apt-get remove -y --purge software-properties-common \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& echo "env[XDEBUG_CONFIG] = \$XDEBUG_CONFIG" >>
/etc/php/7.2/fpm/pool.d/www.conf \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& echo "127.0.0.1 localhost" >> /etc/hosts  
  
COPY certs/server.crt certs/server.key /etc/nginx/  
COPY default /etc/nginx/sites-available/default  
COPY php-fpm.conf /etc/php/7.2/fpm/php-fpm.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80 443  
  
CMD ["/usr/bin/supervisord"]

