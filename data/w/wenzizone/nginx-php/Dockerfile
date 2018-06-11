FROM wenzizone/base  
MAINTAINER wenzizone <wenzizone@126.com>  
RUN apt-get update && \  
apt-get install -y nginx php5-cli php5-curl php5-fpm php5-gd php5-mcrypt
php5-mysql && \  
apt-get clean  
  
ADD supervisord-nginx.conf /etc/supervisor/conf.d/nginx.conf  
ADD supervisord-php-fpm.conf /etc/supervisor/conf.d/php-fpm.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
RUN sed -i '/daemonize/s/;//' /etc/php5/fpm/php-fpm.conf  
RUN sed -i '/daemonize/s/yes/no/' /etc/php5/fpm/php-fpm.conf  
RUN sed -i '/post_max_size/s/8/100/' /etc/php5/fpm/php.ini  
RUN sed -i '/upload_max_filesize/s/2/100/' /etc/php5/fpm/php.ini  
RUN ln -s /etc/php5/mods-available/mcrypt.ini
/etc/php5/fpm/conf.d/20-mcrypt.ini  
  
VOLUME ["/etc/nginx/conf.d", "/usr/share/nginx/html"]  
EXPOSE 80

