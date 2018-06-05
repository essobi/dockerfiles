FROM alpine:3.4  
MAINTAINER Jim Leirvik <jim@jimleirvik.no>  
  
ENV LANG="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8" \  
TERM="xterm"  
RUN apk -U upgrade && \  
apk --update add \  
php5-cli \  
php5-ctype \  
php5-dom \  
php5-intl \  
php5-json \  
php5-pdo \  
php5-pdo_mysql \  
php5-pdo_pgsql && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/* && \  
echo "date.timezone = UTC" >> /etc/php5/php.ini  
  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["php"]  

