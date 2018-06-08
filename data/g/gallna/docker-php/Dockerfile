FROM phusion/baseimage  
MAINTAINER Tomasz Jonik <tomasz@hurricane.works>  
  
# Install php-7  
RUN export LANG=C.UTF-8 \  
&& add-apt-repository ppa:ondrej/php \  
&& apt-get update \  
&& apt-get install -y php5.6-fpm \  
php5.6-intl php5.6-pgsql php5.6-curl php5.6-mbstring php5.6-mysql \  
php-redis php-memcached php-amqp php-uuid php-xdebug \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy configuration files  
ADD php-fpm.conf /etc/php/5.6/fpm/php-fpm.conf  
ADD pool.d /etc/php/5.6/fpm/pool.d/  
  
RUN ln -sf /dev/stdout /var/log/access.log \  
&& ln -sf /dev/stderr /var/log/php5.6-fpm.log  
  
CMD ["php-fpm5.6"]  
  
EXPOSE 9000  

