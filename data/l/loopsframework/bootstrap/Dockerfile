# Dockerfile  
# This file is part of the loops framework.  
#  
# @author Lukas <lukas@m-t.com>  
# @license
https://raw.githubusercontent.com/loopsframework/base/master/LICENSE  
# @link https://github.com/loopsframework/base  
FROM ubuntu:xenial  
  
# Install packages  
RUN apt-get update && \  
apt-get --yes upgrade && \  
apt-get --yes install php7.0-fpm \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-sqlite \  
php7.0-imap \  
php7.0-intl \  
php-redis \  
php-apcu \  
php-mdb2 \  
php-mdb2-driver-mysql \  
php-mdb2-driver-pgsql \  
nginx \  
git \  
supervisor \  
curl \  
redis-server \  
ssl-cert \  
rsyslog \  
libxrender1 \  
xvfb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# Prepare loops directory  
WORKDIR /opt/loops  
  
# Install Loops  
RUN composer create-project loopsframework/bootstrap:dev-master . && \  
composer require loopsframework/extra:dev-master && \  
composer require loopsframework/jobs:dev-master && \  
composer require mikehaertl/phpwkhtmltopdf:^2 && \  
composer require swiftmailer/swiftmailer:^5 && \  
composer require h4cc/wkhtmltopdf-amd64:^0  
  
# Default config directives for extra libraries that work in this environment  
RUN echo "" >> /opt/loops/app/config/config.ini && \  
echo "" >> /opt/loops/app/config/config.ini && \  
echo "[pdf]" >> /opt/loops/app/config/config.ini && \  
echo "binary = wkhtmltopdf-amd64" >> /opt/loops/app/config/config.ini && \  
echo "enableXvfb = true" >> /opt/loops/app/config/config.ini  
  
# Save initial state of app  
RUN mv /opt/loops/app /opt/loops/app_skeleton  
  
# Copy config files  
COPY nginx/nginx.conf /etc/nginx/  
COPY nginx/snippets/* /etc/nginx/snippets/  
COPY redis/redis.conf /etc/redis/  
COPY supervisor/supervisord.conf /etc/supervisor/  
COPY supervisor/conf.d/* /etc/supervisor/conf.d/  
COPY php-fpm/php-fpm.conf /etc/php/7.0/fpm/  
COPY php-fpm/www.conf /etc/php/7.0/fpm/pool.d/  
COPY init.sh /  
COPY nginx.template /  
COPY nginx.template-ssl /  
  
# add vendor/bin to path variable  
ENV PATH /opt/loops/vendor/bin:$PATH  
  
  
# setup app folder as docker volume  
VOLUME "/opt/loops/app"  
  
# run the supervisor manager  
ENTRYPOINT [ "/init.sh" ]  
  
#expose http/https port  
EXPOSE 80 443

