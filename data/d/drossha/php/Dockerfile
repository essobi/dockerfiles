FROM ubuntu  
  
RUN apt-get update && \  
apt-get install software-properties-common -y && \  
add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get -y --no-install-recommends --allow-unauthenticated install \  
php-redis \  
php-imagick \  
php-zmq \  
php-zip \  
php-curl \  
php7.1 \  
php7.1-cli \  
php7.1-fpm \  
php7.1-intl \  
php7.1-bcmath \  
php7.1-bz2 \  
php7.1-pgsql \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-xml \  
php7.1-xmlrpc \  
php7.1-gd && \  
apt-get -y -f purge software-properties-common \  
&& apt-get -y autoremove && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/* /usr/share/doc/*  
  
COPY ./php-overrides.ini /etc/php/7.1/cli/conf.d/90-overrides.ini  
COPY ./php-overrides.ini /etc/php/7.1/fmp/conf.d/90-overrides.ini  
  
CMD ["php", "-a"]  
  
# Configure FPM to run properly on docker  
RUN sed -i "/listen = .*/c\listen = [::]:9000"
/etc/php/7.1/fpm/pool.d/www.conf \  
&& sed -i "/;access.log = .*/c\access.log = /proc/self/fd/2"
/etc/php/7.1/fpm/pool.d/www.conf \  
&& sed -i "/;clear_env = .*/c\clear_env = no" /etc/php/7.1/fpm/pool.d/www.conf
\  
&& sed -i "/;catch_workers_output = .*/c\catch_workers_output = yes"
/etc/php/7.1/fpm/pool.d/www.conf \  
&& sed -i "/pid = .*/c\;pid = /run/php/php7.1-fpm.pid" /etc/php/7.1/fpm/php-
fpm.conf \  
&& sed -i "/;daemonize = .*/c\daemonize = no" /etc/php/7.1/fpm/php-fpm.conf \  
&& sed -i "/error_log = .*/c\error_log = /proc/self/fd/2"
/etc/php/7.1/fpm/php-fpm.conf \  
&& usermod -u 1000 www-data  
  
# The following runs FPM and removes all its extraneous log output on top of
what your app outputs to stdout  
CMD /usr/sbin/php-fpm7.1 -F -O 2>&1 | sed -u 's,.*: \"\\(.*\\)$,\1,'| sed -u
's,"$,,' 1>&1  
  
EXPOSE 9000  

