FROM eboraas/apache-php  
  
MAINTAINER Luca Mattivi <luca@smartdomotik.com>  
  
RUN apt-get update && apt-get install -yqq --force-yes php5-curl  
  
RUN rm /var/www/html/index.html  
COPY index.php /var/www/html/index.php  
  
# Port to expose  
EXPOSE 80  
# Remove pre-existent apache pid and start apache  
CMD rm -f $APACHE_PID_FILE && /usr/sbin/apache2ctl -D FOREGROUND

