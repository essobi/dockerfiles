FROM debian:jessie  
  
MAINTAINER Vincent Chalamon <vincentchalamon@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
git \  
curl \  
nginx \  
sqlite3 \  
libcurl4-openssl-dev \  
pkg-config \  
make \  
php5 \  
php5-curl \  
php5-dev \  
php5-fpm \  
php5-intl \  
php5-sqlite \  
php5-pgsql \  
php5-mysql \  
php5-memcache \  
php5-apcu \  
php5-gd \  
php5-mcrypt \  
php-twig \  
php-pear \  
php-apc \  
supervisor \  
&& pecl install mongo \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure PHP-FPM & Nginx  
RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf
\  
&& sed -e 's/;listen\\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf \  
&& sed -e 's/;listen\\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf \  
&& echo "opcache.enable=1" >> /etc/php5/mods-available/opcache.ini \  
&& echo "opcache.enable_cli=1" >> /etc/php5/mods-available/opcache.ini \  
&& echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# Enable MongoDB PHP  
RUN echo "extension=mongo.so" > /etc/php5/mods-available/mongo.ini  
RUN php5enmod mcrypt mongo  
  
RUN sed -i -e "s/\\(post_max_size =\\).*/\1 50M/g" /etc/php5/cli/php.ini  
RUN sed -i -e "s/\\(upload_max_filesize =\\).*/\1 50M/g" /etc/php5/cli/php.ini  
RUN sed -i -e "s/\\(max_execution_time =\\).*/\1 300/g" /etc/php5/cli/php.ini  
RUN sed -i -e "s/\\(post_max_size =\\).*/\1 50M/g" /etc/php5/fpm/php.ini  
RUN sed -i -e "s/\\(upload_max_filesize =\\).*/\1 50M/g" /etc/php5/fpm/php.ini  
RUN sed -i -e "s/\\(max_execution_time =\\).*/\1 300/g" /etc/php5/fpm/php.ini  
  
ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf  
ADD vhost.conf /etc/nginx/sites-available/default  
  
RUN usermod -u 1000 www-data  
RUN usermod -a -G users www-data  
  
VOLUME /var/www  
WORKDIR /var/www  
  
RUN chown -R www-data:www-data /var/www  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  

