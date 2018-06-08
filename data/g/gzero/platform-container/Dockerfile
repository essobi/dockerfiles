FROM ubuntu:16.04  
  
MAINTAINER Adrian Skierniewski <adrian.skierniewski@gmail.com>  
  
# Set correct environment variables  
ENV HOME /root  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV LARAVEL_LOG_STREAM="/tmp/laravel.log"  
  
RUN apt-get update && \  
apt-get install -y software-properties-common --no-install-recommends && \  
LANG=C.UTF-8 add-apt-repository ppa:nginx/stable && \  
LANG=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y \  
sudo \  
nano \  
htop \  
git \  
cron \  
supervisor \  
nginx \  
gettext \  
curl \  
mysql-client \  
php7.2-fpm \  
php7.2-cli \  
php7.2-common \  
php7.2-curl \  
php7.2-gd \  
php7.2-intl \  
php7.2-json \  
php7.2-ldap \  
php7.2-mbstring \  
php7.2-mysql \  
php7.2-pgsql \  
php7.2-opcache \  
php7.2-xdebug \  
php7.2-xml \  
php7.2-redis \  
php7.2-zip && \  
apt-get remove --purge -y software-properties-common && \  
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
  
# Add logs wrapper  
ADD ./cfg/laravel-logs.sh /var/laravel-logs.sh  
  
# Add cron file  
ADD ./cfg/laravel-cron /var/laravel-cron  
  
RUN chmod 0644 /var/laravel-cron \  
&& chmod +x /var/laravel-logs.sh \  
&& crontab -u www-data /var/laravel-cron \  
&& /usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php \  
&& /bin/mv composer.phar /usr/local/bin/composer \  
&& chmod +x /start.sh \  
&& mv /var/www/html /var/www/public \  
&& mv /var/www/public/index.nginx-debian.html /var/www/public/index.html \  
&& mkfifo $LARAVEL_LOG_STREAM \  
&& chmod 777 $LARAVEL_LOG_STREAM  
  
EXPOSE 80  
  
CMD ["/bin/bash", "/start.sh"]  

