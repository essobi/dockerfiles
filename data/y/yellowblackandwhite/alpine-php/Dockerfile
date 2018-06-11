FROM yellowblackandwhite/alpine-nginx  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
  
RUN apk --update add ca-certificates \  
php php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl \  
php-pdo_mysql php-mysqli php-gd php-iconv php-mcrypt  
  
# fix php-fpm "Error relocating /usr/bin/php-fpm: __flt_rounds: symbol not
found" bug  
RUN apk add -u musl  
RUN rm -rf /var/cache/apk/*  
  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/php-fpm.conf /etc/php/php-fpm.conf  
# ADD config/sites/*.conf /etc/nginx/sites-enabled/  
# ADD service/nginx/run /etc/service/nginx/run  
# ADD service/php-fpm/run /etc/service/php-fpm/run  
# RUN chmod +x /etc/service/nginx/run \  
# && chmod +x /etc/service/php-fpm/run  

