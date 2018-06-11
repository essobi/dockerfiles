FROM phusion/baseimage:latest  
MAINTAINER Marcin Jędrzejewski <marcin.jedrzejewski85@gmail.com>  
  
ENV PHP_MEMORY_LIMIT 128M  
ENV PHP_PM dynamic  
ENV PHP_PM_MAX_CHILDREN 10  
ENV PHP_PM_START_SERVERS 3  
ENV PHP_PM_MIN_SPARE_SERVERS 3  
ENV PHP_PM_MAX_SPARE_SERVERS 10  
ENV PHP_PM_MAX_REQUESTS 120  
ENV PHP_POST_MAX 32M  
ENV PHP_UPLOAD_MAX 128M  
ENV PHP_MAX_EXEC_TIME 300  
ENV REALPATH_CACHE_SIZE 1M  
ENV REALPATH_CACHE_TTL 300  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN add-apt-repository -y ppa:nginx/stable && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apt-utils  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
dbus \  
dnsutils \  
nginx \  
php7.0 \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-soap \  
php7.0-xml \  
ssmtp && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
RUN mkdir -p /etc/nginx/sites-enabled /etc/nginx/sites-available /var/www/html
/run/php  
  
COPY conf/nginx/ /etc/nginx/  
COPY conf/php/ /etc/php/  
COPY conf/cron/ /var/spool/cron/  
COPY bin/setup /etc/my_init.d/  
COPY bin/service/ /etc/service/  
  
RUN chmod +x /etc/service/nginx/run && \  
chmod +x /etc/service/php-fpm/run && \  
chmod +x /etc/my_init.d/setup && \  
phpenmod mcrypt  
  
CMD ["/sbin/my_init"]

