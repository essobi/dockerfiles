FROM goodrainapps/alpine:3.6  
# install nginx and php  
RUN set -x \  
&& apk add --no-cache \  
php5 \  
php5-cli \  
php5-fpm \  
php5-pdo \  
php5-pdo_mysql \  
php5-mysqli \  
php5-json \  
php5-opcache \  
nginx \  
&& mkdir /run/nginx/ -pv  
  
# prepare phpmyadmin package  
ENV PMA_VER 4.7.1  
ENV PMA_URL
https://files.phpmyadmin.net/phpMyAdmin/${PMA_VER}/phpMyAdmin-${PMA_VER}-all-
languages.tar.gz  
ENV PMA_SHA256
de1f4a9c1f917ae63b07be4928d9b9dba7f29c51b1e1be3ed351d1bc278a8b28  
  
RUN mkdir /app \  
&& curl -o /tmp/phpmyadmin.tar.gz -L ${PMA_URL} \  
&& cd /tmp/ \  
&& echo "$PMA_SHA256 phpmyadmin.tar.gz" | sha256sum -c - \  
&& tar xzf phpmyadmin.tar.gz \  
&& mv phpMyAdmin* /app/phpmyadmin \  
&& rm phpmyadmin.tar.gz  
  
COPY etc etc  
COPY config.inc.php /app/phpmyadmin/  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 80  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

