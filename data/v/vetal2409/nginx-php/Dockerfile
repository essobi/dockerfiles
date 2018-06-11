FROM ubuntu:16.04  
MAINTAINER Vitalii Sydorenko <vetal.sydo@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PHP_XDEBUG_REMOTE_AUTOSTART 1  
ENV PHP_CLI_MEMORY_LIMIT 512M  
ENV PHP_FPM_MEMORY_LIMIT 512M  
  
  
# install dependency  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties \  
&& apt-get install -y language-pack-en-base  
RUN LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php  
  
# install packages  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install \  
nano \  
tree \  
curl \  
apt-transport-https \  
wget \  
git \  
supervisor \  
nginx \  
acl \  
iproute2 \  
wkhtmltopdf \  
mongodb \  
php7.1-fpm php7.1-cli php7.1-common php7.1-curl php7.1-gd php7.1-intl
php7.1-json php7.1-mbstring php7.1-mcrypt \  
php7.1-mysql php7.1-opcache php7.1-pgsql php7.1-soap php7.1-sqlite3 php7.1-xml
php7.1-xmlrpc php7.1-xsl php7.1-zip \  
php7.1-mongodb php7.1-redis php7.1-imap php7.1-memcached php7.1-xdebug
php7.1-exif php7.1-readline php7.1-bcmath  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
  
# clear apt cache and remove unnecessary packages  
RUN apt-get autoclean && apt-get -y autoremove  
  
RUN addgroup --system nginx && \  
adduser --system --home /var/cache/nginx --shell /sbin/nologin --disabled-
password --ingroup nginx nginx  
## NGINX configuration  
# redo directory structure  
RUN mkdir -p /etc/nginx/sites \  
&& mv /etc/nginx/sites-available/default /etc/nginx/sites/default.nginx \  
&& rm -r /etc/nginx/sites-available /etc/nginx/sites-enabled  
  
# Forward nginx request and errors logs to stdout|stderr  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& chown -R nginx:nginx /var/log/nginx  
  
# Copy crontabs  
COPY config/crontabs /var/spool/cron/crontabs  
  
# bakup configurations  
RUN cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak  
# copy new configurations  
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf  
# create php virtual host  
RUN mkdir -p /opt/app && echo "<?php phpinfo();" >> /opt/app/index.php  
COPY config/nginx/sites/php.nginx /etc/nginx/sites/php.nginx  
  
## PHP configuration  
# bakup configurations  
RUN cp /etc/php/7.1/fpm/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf.bak \  
&& cp /etc/php/7.1/fpm/pool.d/www.conf /etc/php/7.1/fpm/pool.d/www.conf.bak \  
&& cp /etc/php/7.1/fpm/php.ini /etc/php/7.1/fpm/php.ini.bak \  
&& cp /etc/php/7.1/cli/php.ini /etc/php/7.1/cli/php.ini.bak  
# copy new configurations  
COPY config/php/fpm/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
COPY config/php/fpm/pool.d/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
COPY config/php/fpm/php.ini /etc/php/7.1/fpm/php.ini  
COPY config/php/cli/php.ini /etc/php/7.1/cli/php.ini  
COPY config/php/mods-available/xdebug.ini /etc/php/7.1/mods-
available/xdebug.ini  
# php7.1-fpm will not start if this directory does not exist  
RUN mkdir /run/php  
# mods configuration  
RUN phpdismod xdebug  
RUN echo "export PHP_IDE_CONFIG=\"serverName=server\"" >> ~/.bashrc  
  
## Supervisor configuration  
# copy config file for Supervisor  
COPY config/supervisor/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
WORKDIR /opt/app  
  
# NGINX ports  
EXPOSE 80  
COPY scripts /var/scripts  
  
RUN mv /var/scripts/wait-for-it.sh /usr/bin/waitforit  
  
RUN mv /var/scripts/xdebug.sh /usr/local/bin/xdebug  
RUN chmod +x /usr/local/bin/xdebug  
  
RUN mv /var/scripts/start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start.sh  
CMD ["start.sh"]  

