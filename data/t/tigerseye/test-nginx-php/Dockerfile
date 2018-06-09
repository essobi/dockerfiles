FROM alpine:3.7  
  
###### Install packages  
RUN apk --no-cache add php7 php7-fpm php7-mysqli php7-opcache php7-common
php7-mcrypt php7-json php7-openssl php7-curl \  
php7-bz2 php7-zip php7-dev php7-zlib php7-xml php7-simplexml php7-phar
php7-intl php7-dom php7-xmlreader php7-xmlwriter php7-ctype php7-pdo
php7-pdo_mysql php7-bcmath\  
php7-memcached php7-redis php7-pgsql php7-pdo_pgsql php7-mbstring php7-gd
php7-tokenizer php7-simplexml php7-calendar mysql-client nginx supervisor curl
bash  
  
###### set up timezone  
RUN apk update && apk add ca-certificates && \  
apk add tzdata && \  
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone  
  
  
###### Chaning timezone ######  
RUN set -x && \  
unlink /etc/localtime && \  
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
###### supervisord ######  
ADD supervisord.conf /etc/supervisord.conf  
  
###### startup prepare ######  
VOLUME ["/var/www/html", "/etc/nginx/conf.d", "/etc/php7/php-fpm.d"]  
  
EXPOSE 80 443  
WORKDIR /var/www/html  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

