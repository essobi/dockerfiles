FROM alpine:3.6  
MAINTAINER "Michel Behlok"  
RUN apk update  
  
RUN apk add php7-fpm php7-gd php7-zip php7-pdo php7-pdo_mysql php7-opcache
nginx php7-json php7-session php7-ctype php7-curl php7-dom php7-tokenizer
php7-redis php7-xml  
  
RUN apk add --update openssl  
  
RUN mkdir -p /run/nginx  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /etc/php7/conf.d/opcache-recommended.ini  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \ && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
ADD start.sh /start.sh  
  
ENTRYPOINT ["sh","/start.sh"]  

