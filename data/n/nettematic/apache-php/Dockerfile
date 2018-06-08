FROM nettematic/php:7.2  
MAINTAINER Jan Harsa <j.harsa@gmail.com>  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN apt-get update && apt-get update -y && \  
# APACHE ###################################################################  
apt-get install -y apache2 apache2-mod-php7.2  
RUN a2enmod include && \  
a2enmod rewrite && \  
a2enmod ssl && \  
a2enmod proxy_fcgi && \  
a2enmod php7.2 && \  
rm /etc/apache2/sites-enabled/000-default.conf && \  
#rm /etc/apache2/sites-enabled/default-ssl.conf && \  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /var/lib/log/* /tmp/* /var/tmp/*  
  
VOLUME /srv  
WORKDIR /srv  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 9001  
RUN ["supervisord", "--configuration", "/etc/supervisor/supervisord.conf"]  
CMD ["apache2ctl", "-D FOREGROUND"]  
  

