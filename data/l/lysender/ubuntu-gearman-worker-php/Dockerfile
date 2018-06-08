FROM lysender/ubuntu-php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN apt-get -y install supervisor \  
libevent-2.0-5 \  
libgearman-dev \  
php5-gearman \  
php5-memcached && apt-get clean  
  
# Enable php modules  
RUN php5enmod gearman  
RUN php5enmod memcached  
  
# Configure servicies  
ADD ./start.sh /start.sh  
RUN mkdir -p /etc/supervisor/conf.d  
ADD ./supervisor-phpworker.conf /etc/supervisor/conf.d/phpworker.conf  
  
RUN chmod 755 /start.sh  
  
RUN mkdir -p /var/www/scripts  
ADD ./worker.php /var/www/scripts/worker.php  
  
RUN mkdir -p /var/log/supervisor  
  
VOLUME ["/var/www/scripts", "/var/log/supervisor"]  
  
CMD ["/bin/bash", "/start.sh"]  
  

