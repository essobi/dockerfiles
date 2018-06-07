FROM wordpress:fpm-alpine  
  
RUN apk add --no-cache curl runit nginx  
  
ADD start_runit /sbin/  
  
COPY ./var/ /var  
  
COPY ./etc/ /etc  
  
RUN chmod a+x /sbin/start_runit && mkdir /etc/runit_init.d  
  
RUN echo "define('DISABLE_WP_CRON', true);" >> /usr/src/wordpress/wp-config-
sample.php  
  
VOLUME /var/www/html  
  
EXPOSE 80  
CMD ["/sbin/start_runit"]  

