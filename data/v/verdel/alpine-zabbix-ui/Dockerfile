FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
ENV DB_HOST localhost  
ENV DB_PORT 3306  
ENV DB_USER zabbix  
ENV DB_PASS zabbix  
ENV ZABBIX_SERVER localhost  
ENV ZABBIX_PORT 10051  
ENV HTTP_FQDN localhost  
  
# Copy init scripts  
COPY rootfs /  
  
# Install zabbix  
RUN apk --update add \  
bash \  
apache2 \  
php5 \  
php5-mysqli \  
php5-apache2 \  
php5-ctype \  
php5-bcmath \  
php5-gd \  
php5-sockets \  
php5-xmlreader \  
zabbix-webif@community \  
# Clean up  
&& rm -rf \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/*  
  
# Remove ssl configuration  
RUN rm -f /etc/apache2/conf.d/ssl.conf  
  
# Create folder for apache2 pid file  
RUN mkdir /run/apache2  
  
# Export ports  
EXPOSE 80/tcp  

