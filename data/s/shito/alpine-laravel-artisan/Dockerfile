FROM shito/alpine-php7-cli:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
# Add PHP 7  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
php7-mcrypt \  
php7-mongodb \  
php7-mysqlnd \  
php7-pgsql \  
php7-redis \  
php7-sqlite3 \  
php7-mbstring \  
php7-iconv \  
php7-gd  
  
RUN rm -fr /var/cache/apk/*  
  
WORKDIR /usr/share/nginx/html  
  
ENTRYPOINT ["php", "artisan"]  
CMD ["--help"]

