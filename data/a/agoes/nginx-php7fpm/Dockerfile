FROM ubuntu:latest  
  
MAINTAINER Aswari Agoes <agoes.aswari@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install nginx, php7-fpm and other php extensions  
RUN apt-get update -y && \  
apt-get install -y software-properties-common supervisor nginx && \  
add-apt-repository ppa:ondrej/php-7.0 && \  
apt-get update -y && \  
apt-get install -y --force-yes php7.0-fpm php7.0-cli php-redis php-memcached
php7.0-mysql php-gd php-imagick php-curl php-mcrypt && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# install extensions  
RUN phpenmod redis memcached mysql gd imagick curl mcrypt  
  
# configuration  
RUN sed -i 's/^listen\s*=.*$/listen = \/var\/run\/php\/php7.0-fpm.sock/'
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i
's/\;error_log\s*=\s*syslog\s*$/error_log\s*=\s*\/var\/log\/php7\/error.log/'
/etc/php/7.0/fpm/php.ini && \  
sed -i 's/^\display_errors\s*=\s*Off\s*$/display_errors\ =\ On/'
/etc/php/7.0/fpm/php.ini && \  
sed -i 's/access_log\s*\/var\/log\/nginx\/access.log;$/#\ access_log\
\/var\/log\/nginx\/access.log;/' /etc/nginx/nginx.conf  
  
# create php-fpm sock file  
RUN mkdir /var/run/php/ && \  
touch /var/run/php/php7.0-fpm.sock  
  
COPY supervisor/conf.d/supervisord.conf /etc/supervisor/conf.d/  
  
VOLUME ["/var/www", "/var/log/php7", "/var/log/nginx"]  
  
WORKDIR /var/www  
  
EXPOSE 80  
# add nginx server block  
COPY nginx/sites-available/default.conf /etc/nginx/sites-available/default  
RUN ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
  
CMD ["supervisord"]  

