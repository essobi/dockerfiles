FROM php:7.1.5-alpine  
RUN set -ex \  
&& apk --no-cache add postgresql-dev \  
&& docker-php-ext-install pdo pdo_mysql pdo_pgsql  
  
WORKDIR /var/www  
RUN curl --connect-timeout 120 -m 120 -L -o /var/www/index.php
https://github.com/vrana/adminer/releases/download/v4.6.2/adminer-4.6.2.php  
RUN curl --connect-timeout 120 -m 120 -o /var/www/adminer.css
https://raw.githubusercontent.com/arcs-/Adminer-Material-
Theme/master/adminer.css  
  
EXPOSE 8080  
ENTRYPOINT ["php", "-S", "0.0.0.0:8080"]  

