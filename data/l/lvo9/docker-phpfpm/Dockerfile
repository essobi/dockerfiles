FROM php:5.6-fpm  
  
RUN sed -i 's/error_log/; error_log/' /usr/local/etc/php-fpm.d/docker.conf  
RUN sed -i 's/access.log/; access.log/' /usr/local/etc/php-fpm.d/docker.conf  
RUN sed -i 's/catch_workers_output/; catch_workers_output/'
/usr/local/etc/php-fpm.d/docker.conf  
  
RUN sed -i 's/;php_flag\\[display_errors\\] = off/php_flag\\[display_errors\\]
= off/' /usr/local/etc/php-fpm.d/www.conf  
RUN sed -i 's/;php_admin_flag\\[log_errors\\] =
on/php_admin_flag\\[log_errors\\] = on/' /usr/local/etc/php-fpm.d/www.conf  

