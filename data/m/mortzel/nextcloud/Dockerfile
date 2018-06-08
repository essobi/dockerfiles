FROM alpine:latest  
  
RUN apk --no-cache add apache2 openssl php5-apache2 php5-pdo php5-pdo_mysql
php5-gd php5-json php5-mysql php5-curl php5-intl php5-mcrypt php5-imagick
php5-zip php5-dom php5-xmlreader php5-zlib php5-iconv php5-ctype php5-xml
samba-client  
RUN mkdir /run/apache2  
RUN chown apache: /run/apache2  
COPY start.sh /  
  
VOLUME "/var/www/localhost/htdocs"  
  
EXPOSE 80 443  
CMD ["/bin/sh", "/start.sh"]  

