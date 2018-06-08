# Debian: essential  
#  
# VERSION 0.1  
# Pull the base image.  
FROM giordan/d-essentials  
  
MAINTAINER Gabriele Giuranno <gabrielegiuranno@gmail.com>  
  
# Set environment variables.  
ENV FILES conf/  
ENV TERM xterm-256color  
  
RUN apt-get update  
RUN apt-get update && apt-get install -y \  
mysql-client \  
php5-cli \  
php5-fpm \  
php5-curl \  
php5-mcrypt \  
php5-mysql \  
php5-gd \  
php5-intl  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ${FILES}php-app.ini /etc/php5/fpm/conf.d/  
ADD ${FILES}php-app.ini /etc/php5/cli/conf.d/  
ADD ${FILES}php-app.pool.conf /etc/php5/fpm/pool.d/  
  
RUN rm -rf /etc/php5/fpm/pool.d/www.conf  
RUN usermod -u 1000 www-data  
  
ADD start.sh /usr/local/bin/start.sh  
  
# Configure executable to start php5-fpm.  
CMD ["start.sh"]  
  
# Expose ports.  
EXPOSE 9000  

