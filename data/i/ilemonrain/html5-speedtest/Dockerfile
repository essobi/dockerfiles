FROM alpine  
  
LABEL MAINTAINER iLemonrain <ilemonrain@ilemonrain.com>  
  
RUN (apk --no-cache upgrade ;\  
apk add php7-apache2 curl php7-cli php7-json php7-phar php7-openssl
php7-mbstring php7-zlib ;\  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer ;\  
sed -i "s/AllowOverride none/AllowOverride All/" /etc/apache2/httpd.conf ;\  
rm -f /var/www/localhost/htdocs/* ;\  
mkdir /run/apache2/ ;\  
rm -f /var/cache/apk/* )  
  
ADD entrypoint.sh /entrypoint.sh  
ADD speedtest/* /var/www/localhost/htdocs/  
  
RUN (chown -R apache:apache /var/www/localhost/htdocs/ ;\  
chmod 755 /entrypoint.sh )  
  
EXPOSE 80  
ENTRYPOINT [ "sh", "/entrypoint.sh" ]  

