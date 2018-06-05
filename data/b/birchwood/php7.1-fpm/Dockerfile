FROM birchwood/php7.1:latest  
  
# Install FPM  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install php7.1-fpm \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*  
  
# Install selected extensions and other stuff  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php-memcached php7.1-mysql
php7.1-pgsql php-redis php7.1-sqlite3 php7.1-bcmath php7.1-bz2 php7.1-dba
php7.1-gd php7.1-imap php-imagick php7.1-intl php7.1-ldap php7.1-mbstring
php7.1-odbc php7.1-phpdbg php7.1-recode php7.1-soap php7.1-sybase php7.1-tidy
php-yaml php-xdebug \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
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
# Open up fcgi port  
EXPOSE 9000

