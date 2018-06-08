FROM marvambass/phpmyadmin  
  
RUN sed -i 's/post_max_size = 8M/post_max_size = 2000M/g'
/etc/php5/fpm/php.ini  
RUN sed -i 's/http {/http {client_max_body_size 24000M;/g'
/etc/nginx/nginx.conf  

