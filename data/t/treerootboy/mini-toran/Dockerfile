FROM alpine:latest  
MAINTAINER LM <treerootboy@gmail.com>  
  
RUN apk add --update tar wget openssl php-json php-openssl nginx php-fpm php-
ctype php-dom \  
&& rm -rf /var/cache/apk/* \  
&& wget --no-check-certificate https://toranproxy.com/releases/toran-
proxy-v1.1.7.tgz \  
&& tar xzf toran-proxy-v1.1.7.tgz \  
&& rm -f toran-proxy-v1.1.7.tgz \  
&& adduser -u8080 -D -H www \  
&& cd /toran \  
&& chown www:root app/toran app/cache app/logs web/repo
app/bootstrap.php.cache \  
&& cp app/config/parameters.yml.dist app/config/parameters.yml \  
&& sed -i 's/nobody/www/g' /etc/php/php-fpm.conf \  
&& sed -i 's/pm = dynamic/pm = static/g' /etc/php/php-fpm.conf \  
&& sed -i 's/pm.max_children = 5/pm.max_children = 10/g' /etc/php/php-fpm.conf
\  
&& sed -i 's/;events.mechanism = epoll/events.mechanism = epoll/g'
/etc/php/php-fpm.conf  
  
WORKDIR /toran  
VOLUME /toran/app/toran  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT php-fpm && nginx -g "daemon off;"  
  

