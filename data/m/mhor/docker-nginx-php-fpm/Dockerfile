FROM tutum/nginx:latest  
  
# Install packages  
RUN apt-get update  
RUN apt-get install -y supervisor curl wget php5-fpm php5-mysql php5-mcrypt
php5-gd php5-memcached php5-curl php5-xdebug  
  
# Create required directories  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /var/run/php5-fpm  
  
RUN echo "date.timezone= Europe/Paris" >> /etc/php5/fpm/php.ini  
RUN touch /etc/php5/fpm/conf.d/40-custom.ini  
RUN echo "zend_extension = xdebug.so" >> /etc/php5/fpm/conf.d/40-custom.ini  
RUN echo "xdebug.remote_enable = 1" >> /etc/php5/fpm/conf.d/40-custom.ini  
RUN echo "xdebug.renite_enable = 1" >> /etc/php5/fpm/conf.d/40-custom.ini  
RUN echo "xdebug.max_nesting_level = 1000" >>
/etc/php5/fpm/conf.d/40-custom.ini  
RUN echo "xdebug.profiler_enable_trigger = 1" >>
/etc/php5/fpm/conf.d/40-custom.ini  
RUN echo "xdebug.profiler_output_dir = \"/var/log\"" >>
/etc/php5/fpm/conf.d/40-custom.ini  
  
RUN touch /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[supervisord]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[program:nginx]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "command = /usr/sbin/nginx" >>
/etc/supervisor/conf.d/supervisord.conf  
RUN echo "user = root" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "autostart = true" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "[program:php5-fpm]" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "command = /usr/sbin/php5-fpm" >>
/etc/supervisor/conf.d/supervisord.conf  
RUN echo "user = root" >> /etc/supervisor/conf.d/supervisord.conf  
RUN echo "autostart = true" >> /etc/supervisor/conf.d/supervisord.conf  
  
RUN cd /tmp && \  
php -r "readfile('https://getcomposer.org/installer');" | php && \  
mv composer.phar /usr/local/bin/composer  
  
# Expose volumes  
VOLUME ["/var/www", "/etc/nginx/sites-enabled"]  
  
EXPOSE 80 9000  
CMD ["/usr/bin/supervisord"]  

