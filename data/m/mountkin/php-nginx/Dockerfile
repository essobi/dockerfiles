FROM php:7-fpm  
RUN apt-get update && \  
apt-get install -y --no-install-recommends nginx curl ca-certificates && \  
rm -r /var/cache/apt /var/lib/apt/lists/*  
  
ARG S6_URL=https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz  
  
RUN curl -L $S6_URL | tar -xz -C /  
ADD services.d /etc/services.d  
ADD conf/nginx.conf /etc/nginx/  
ADD conf/zz-docker.conf /usr/local/etc/php-fpm.d/  
ADD www/index.php /var/www/html/  
  
ENTRYPOINT ["/init"]  

