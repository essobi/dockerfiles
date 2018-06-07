FROM mckaynz/php7-base  
MAINTAINER McKay Software <hello@mckaysoftware.co.nz>  
  
RUN sed -i 's|DocumentRoot /var/www/html|DocumentRoot /var/www/html/public|' \  
/etc/apache2/sites-enabled/000-default.conf  
  
ENV APP_LOG errorlog  
ENV CACHE_DRIVER file  
ENV DB_CONNECTION mysql  
ENV QUEUE_DRIVER sync  
ENV SESSION_DRIVER database  
  
ENV MAIL_DRIVER smtp  
ENV MAIL_HOST mailtrap.io  
ENV MAIL_PORT 2525  
ENV MAIL_USERNAME null  
ENV MAIL_PASSWORD null  
ENV MAIL_ENCRYPTION null  
  
ENV REDIS_HOST redis  
ENV REDIS_PASSWORD null  
ENV REDIS_PORT 6379  
COPY ./php-artisan.sh /scripts/setup.d/  
COPY ./laravel-appkey.sh /scripts/start.d/  

