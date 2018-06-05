FROM alpine:3.6  
LABEL Maintainer="Michal Hošna <mh@michalhosna.com>"  
  
RUN apk --no-cache add php5 php5-fpm php5-json \  
php7-mbstring nginx supervisor curl  
  
COPY docker/fpm-pool.conf /etc/php5/fpm.d/fpm-pool.conf  
COPY docker/php.ini /etc/php5/conf.d/php.ini  
COPY docker/nginx.conf /etc/nginx/nginx.conf  
  
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY src /src  
WORKDIR /src  
  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

