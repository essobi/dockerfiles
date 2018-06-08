FROM lysender/php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN yum -y install supervisor \  
libevent \  
gearmand \  
libgearman \  
libgearman-devel \  
php-pecl-gearman && yum clean all  
  
# Configure servicies  
ADD ./start.sh /start.sh  
ADD ./supervisor-phpworker.ini /etc/supervisord.d/phpworker.ini  
ADD ./timezone.ini /etc/php.d/timezone.ini  
  
RUN chmod 755 /start.sh  
  
RUN mkdir -p /var/www/scripts  
ADD ./worker.php /var/www/scripts/worker.php  
  
RUN mkdir -p /var/log/supervisor  
  
VOLUME ["/var/www/scripts", "/var/log/supervisor"]  
  
CMD ["/bin/bash", "/start.sh"]  
  

