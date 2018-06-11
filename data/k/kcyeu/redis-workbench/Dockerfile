FROM kcyeu/apache:latest  
MAINTAINER Kuo-Cheng Yeu <kmd@mikuru.tw>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && apt-get -qqy install \  
redis-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/www/rw  
RUN git clone https://github.com/kcyeu/redis-workbench.git /var/www/rw  
ADD 100-redis-workbench.conf /etc/apache2/sites-available/100-redis-
workbench.conf  
#RUN echo "<?php phpinfo(); ?>" > /var/www/rw/phpinfo.php  
RUN a2ensite 100-redis-workbench  
RUN a2dissite 000-default  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  

