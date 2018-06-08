FROM viison/php-fpm-xdebug:5.6  
RUN echo "xdebug.max_nesting_level=500" >> /etc/php5/mods-available/xdebug.ini  
  
COPY www.conf /etc/php5/fpm/pool.d/  

