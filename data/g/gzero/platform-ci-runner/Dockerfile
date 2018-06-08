FROM ubuntu:16.04  
MAINTAINER Adrian Skierniewski <adrian.skierniewski@gmail.com>  
  
# Set correct environment variables  
ENV HOME /root  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV LARAVEL_LOG_STREAM="/tmp/laravel.log"  
RUN apt-get update && \  
apt-get install -y software-properties-common apt-transport-https wget curl
--no-install-recommends && \  
wget -q -O - https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
LANG=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
LANG=C.UTF-8 add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \  
LANG=C.UTF-8 add-apt-repository "deb [arch=amd64]
https://dl.google.com/linux/chrome/deb/ stable main" && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
docker-ce \  
sudo \  
nano \  
git \  
iproute2 \  
gettext \  
supervisor \  
nginx \  
php7.2-fpm \  
php7.2-cli \  
php7.2-common \  
php7.2-curl \  
php7.2-gd \  
php7.2-intl \  
php7.2-json \  
php7.2-ldap \  
php7.2-mbstring \  
php7.2-pgsql \  
php7.2-opcache \  
php7.2-xdebug \  
php7.2-xml \  
php7.2-redis \  
php7.2-zip \  
build-essential \  
nodejs \  
google-chrome-stable && \  
apt-get remove --purge -y software-properties-common apt-transport-https && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /etc/cron.d/* && \  
rm -rf /etc/cron.hourly/* && \  
rm -rf /etc/cron.daily/* && \  
rm -rf /etc/cron.monthly/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# Nginx config  
ADD ./cfg/nginx.conf /etc/nginx/nginx.conf  
  
# PHP-FPM configs  
ADD ./cfg/php-fpm.conf /etc/php/7.2/fpm/php-fpm.conf  
ADD ./cfg/php.ini /etc/php/7.2/fpm/php.ini  
ADD ./cfg/pool.d/www.conf /etc/php/7.2/fpm/pool.d/www.conf  
ADD ./cfg/xdebug.ini ./etc/php/7.2/mods-available/xdebug.ini  
  
# Supervisor config  
ADD ./cfg/supervisord.conf /etc/supervisord.conf  
  
# Start script  
ADD ./start.sh /start.sh  
  
# Add site template  
ADD ./cfg/site.conf /etc/nginx/conf.d/site.template  
  
RUN /usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php \  
&& /bin/mv composer.phar /usr/local/bin/composer \  
&& chmod +x /start.sh \  
&& mv /var/www/html /var/www/public \  
&& mv /var/www/public/index.nginx-debian.html /var/www/public/index.html \  
&& touch $LARAVEL_LOG_STREAM \  
&& chmod 777 $LARAVEL_LOG_STREAM  
  
CMD ["/bin/bash", "/start.sh"]

