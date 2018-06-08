FROM ubuntu:16.04  
MAINTAINER Adrian Skierniewski <adrian.skierniewski@gmail.com>  
  
# Set correct environment variables  
ENV HOME /root  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
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
supervisor \  
nginx \  
gettext \  
curl \  
mysql-client \  
php7.1-fpm \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-gd \  
php7.1-intl \  
php7.1-json \  
php7.1-ldap \  
php7.1-mcrypt \  
php7.1-mbstring \  
php7.1-mysql \  
php7.1-opcache \  
php7.1-xdebug \  
php7.1-xml \  
php7.1-redis \  
php7.1-zip && \  
apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
RUN phpenmod mcrypt  
  
RUN /usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php  
RUN /bin/mv composer.phar /usr/local/bin/composer  
  
# Nginx config  
ADD ./cfg/nginx.conf /etc/nginx/nginx.conf  
  
# PHP-FPM configs  
ADD ./cfg/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
ADD ./cfg/php.ini /etc/php/7.1/fpm/php.ini  
ADD ./cfg/pool.d/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
ADD ./cfg/xdebug.ini ./etc/php/7.1/mods-available/xdebug.ini  
  
# Supervisor config  
ADD ./cfg/supervisord.conf /etc/supervisord.conf  
  
# Start script  
ADD ./start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Wrapper to run as www-data  
ADD ./commandWrapper.sh /commandWrapper.sh  
RUN chmod +x /commandWrapper.sh  
  
RUN mv /var/www/html /var/www/public  
RUN mv /var/www/public/index.nginx-debian.html /var/www/public/index.html  
  
# Add site templates  
ADD ./cfg/mysite /etc/nginx/conf.d/mysite.template  
ADD ./cfg/mysite-ssl /etc/nginx/conf.d/mysite-ssl.template  
  
EXPOSE 80 443  
CMD ["/bin/bash", "/start.sh"]  

