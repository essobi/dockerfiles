FROM 2dotstwice/nginx  
  
MAINTAINER Kristof Coomans "kristof@2dotstwice.be"  
ENV REFRESHED_AT "2017-09-06 10:24:00"  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing --no-install-
recommends -q install \  
software-properties-common && \  
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
DEBIAN_FRONTEND=noninteractive apt-get -y update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --fix-missing --no-install-
recommends -q install \  
php7.0-fpm \  
php7.0-gd \  
php7.0-sqlite \  
php7.0-mysqlnd \  
php7.0-curl \  
php7.0-intl \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-opcache \  
php7.0-json \  
php7.0-mcrypt \  
php7.0-bcmath \  
php7.0-soap \  
php7.0-zip && \  
rm -rf /var/lib/apt/lists/*  
  
ENV CONFIG_REFRESHED_AT "2017-09-06 10:24:00"  
ENV PHP_CONFIG_DIR /etc/php/7.0  
# php configuration  
ADD ./files/etc/php/fpm/conf.d/99-custom.ini
${PHP_CONFIG_DIR}/fpm/conf.d/99-custom.ini  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
${PHP_CONFIG_DIR}/fpm/php.ini  
  
# php-fpm configuration  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g"
${PHP_CONFIG_DIR}/fpm/php-fpm.conf  
RUN mkdir /run/php  
  
# supervisor configuration for php-fpm  
ADD ./files/etc/supervisor/conf.d/php-fpm.conf /etc/supervisor/conf.d/php-
fpm.conf  
  
# nginx site configuration for php-fpm  
ADD ./files/etc/nginx/sites-available/default /etc/nginx/sites-
available/default  
  
# Standard hosting package nginx configuration  
# Reduce worker processes to 2, it's just a small site with not much traffic.  
RUN sed -i -e "s/worker_processes 4/worker_processes 2/g"
/etc/nginx/nginx.conf  
  
# Standard hosting package php-fpm configuration  
ADD ./files/etc/php/fpm/pool.d/www.conf ${PHP_CONFIG_DIR}/fpm/pool.d/www.conf

