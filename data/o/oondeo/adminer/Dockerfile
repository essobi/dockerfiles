FROM oondeo/php:7  
  
RUN sed -i "s/^upload_max_filesize.*/upload_max_filesize = 1000M/g"
/usr/local/etc/php/php.ini \  
&& sed -i "s/^post_max_size.*/post_max_size = 1000M/g"
/usr/local/etc/php/php.ini \  
&& sed -i "s/^memory_limit.*/memory_limit = -1/g" /usr/local/etc/php/php.ini \  
&& sed -i "s/^max_execution_time.*/max_execution_time = 0/g"
/usr/local/etc/php/php.ini  

