#  
# Php Dockerfile  
#  
# https://github.com/tamboraorg/docker/crephp  
#  
# Pull base image.  
FROM tamboraorg/creubuntu  
  
# Fixes some weird terminal issues such as broken clear / CTRL+L  
ENV TERM=linux  
ENV PHP_VERSION 7.0  
# Install cURL and nano  
#RUN apt-get update \  
# && apt-get install -y --no-install-recommends curl ca-certificates nano \  
# && apt-get clean \  
#&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*  
# Install dotdeb repo, PHP7, composer and selected extensions  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php$PHP_VERSION-cli
php$PHP_VERSION-curl \  
php$PHP_VERSION-json php$PHP_VERSION-mcrypt php$PHP_VERSION-opcache
php$PHP_VERSION-readline php$PHP_VERSION-xml php$PHP_VERSION-zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*  
#CMD ["php", "-a"]  
# If you'd like to be able to use this container on a docker-compose
environment as a quiescent PHP CLI container  
# you can /bin/bash into, override CMD with the following - bear in mind that
this will make docker-compose stop  
# slow on such a container, docker-compose kill might do if you're in a hurry  
# CMD ["tail", "-f", "/dev/null"]  
# Install FPM  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php$PHP_VERSION-fpm \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*  
# File permissions workaround  
RUN usermod -u 1000 www-data  
  
# PHP-FPM packages need a nudge to make them docker-friendly  
COPY overrides.conf /etc/php/$PHP_VERSION/fpm/pool.d/z-overrides.conf  
  
# PHP-FPM has really dirty logs, certainly not good for dockerising  
# The following startup script contains some magic to clean these up  
COPY php-fpm-startup /usr/bin/php-fpm  
CMD /usr/bin/php-fpm  
  
# Open up fcgi port  
EXPOSE 9000  
# Install selected extensions and other stuff  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php$PHP_VERSION-gd
php$PHP_VERSION-mbstring php-imagick php-ssh2 \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
# Install memcached  
# maybe add 'memcached' here as well...  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php-memcached \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
# Install db extensions and other stuff  
# php$PHP_VERSION-apcu php$PHP_VERSION-apcu-bc is depricated  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php-mongodb php$PHP_VERSION-
pgsql \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
WORKDIR "/var/www/cre"

