FROM alpine:edge  
  
ENV TERM xterm  
  
RUN apk add --update curl wget git mysql mysql-client \  
bash nginx ca-certificates \  
php-fpm php-json php-zlib php-xml php-pdo php-phar php-openssl \  
php-pdo_mysql php-mysqli \  
php-gd php-iconv php-mcrypt \  
php-curl php-openssl php-json php-dom php-ctype && \  
apk add -u musl && \  
mkdir -p /var/lib/mysql && \  
mkdir -p /etc/mysql/conf.d && \  
mkdir -p /etc/nginx/conf.d && \  
mkdir -p /var/run/mysql/ && \  
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer && \  
rm -rf /var/cache/apk/*  
  
ADD files/nginx.conf /etc/nginx/  
ADD files/php-fpm.conf /etc/php/  
ADD files/my.cnf /etc/mysql/  
ADD files/default.conf /etc/nginx/conf.d/  
ADD files/run.sh /  
RUN chmod +x /run.sh  
  
EXPOSE 80  
EXPOSE 3306  
WORKDIR /data/htdocs  
VOLUME ["/data/htdocs", "/data/logs", "/var/lib/mysql", "/etc/mysql/conf.d/"]  
CMD ["/run.sh"]  

