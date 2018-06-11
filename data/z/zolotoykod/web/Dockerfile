FROM phpdockerio/php71-fpm:latest  
LABEL maintainer="Constantine Karnaukhov <genteelknight@gmail.com>"  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install \  
php7.1-memcached \  
php7.1-memcache \  
php7.1-mbstring \  
php7.1-mysql \  
php7.1-intl \  
php7.1-xdebug \  
php7.1-interbase \  
php7.1-soap \  
php7.1-gd \  
php7.1-imagick \  
php7.1-mcrypt \  
php7.1-opcache \  
php7.1-zip \  
nginx \  
ssmtp \  
less \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
RUN usermod -u 1000 www-data  
  
COPY php/ /etc/php/7.1/fpm/conf.d/  
COPY php/ /etc/php/7.1/cli/conf.d/  
COPY nginx/ /etc/nginx/  
COPY www/ /var/www/html/  
COPY sbin/ /usr/local/sbin/  
  
WORKDIR "/var/www/html"  
  
RUN chmod +x /usr/local/sbin/entrypoint && chown -R www-data.www-data
/var/www/html  
CMD entrypoint; sleep infinity  
  
EXPOSE 80 443 9000  
# Clean working directory of demo files  
ONBUILD RUN rm -rf ./*  

